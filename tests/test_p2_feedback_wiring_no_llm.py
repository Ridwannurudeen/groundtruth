from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from cognee.infrastructure.session.session_manager import SessionManager
from cognee.modules.graph.cognee_graph.CogneeGraph import CogneeGraph
from cognee.modules.graph.cognee_graph.CogneeGraphElements import Edge, Node
from cognee.tasks.memify.apply_feedback_weights import apply_feedback_weights
from cognee.tasks.memify.extract_feedback_qas import extract_feedback_qas


class InMemoryGraphWithWeights:
    def __init__(self) -> None:
        self.node_weights = {"n1": 0.5}
        self.edge_weights = {"e1": 0.5}

    async def get_node_feedback_weights(self, node_ids):
        return {
            node_id: self.node_weights[node_id]
            for node_id in node_ids
            if node_id in self.node_weights
        }

    async def set_node_feedback_weights(self, node_feedback_weights):
        result = {}
        for node_id, weight in node_feedback_weights.items():
            if node_id in self.node_weights:
                self.node_weights[node_id] = float(weight)
                result[node_id] = True
            else:
                result[node_id] = False
        return result

    async def get_edge_feedback_weights(self, edge_object_ids):
        return {
            edge_id: self.edge_weights[edge_id]
            for edge_id in edge_object_ids
            if edge_id in self.edge_weights
        }

    async def set_edge_feedback_weights(self, edge_feedback_weights):
        result = {}
        for edge_id, weight in edge_feedback_weights.items():
            if edge_id in self.edge_weights:
                self.edge_weights[edge_id] = float(weight)
                result[edge_id] = True
            else:
                result[edge_id] = False
        return result


def add_ranked_edge(
    graph: CogneeGraph,
    edge_id: str,
    *,
    distance: float,
    feedback_weight: float,
) -> Edge:
    node_a = Node(f"{edge_id}-a")
    node_b = Node(f"{edge_id}-b")
    edge = Edge(node_a, node_b, {"edge_object_id": edge_id})
    for element in (node_a, node_b, edge):
        element.attributes["vector_distance"] = [distance]
        element.attributes["importance_weight"] = 1.0
        element.attributes["feedback_weight"] = feedback_weight
    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_edge(edge)
    return edge


@pytest.mark.asyncio
async def test_feedback_weights_shift_graph_ranking_without_llm(tmp_path) -> None:
    from cognee.infrastructure.databases.cache.sql.SqlCacheAdapter import (
        SqlCacheAdapter,
    )

    adapter = SqlCacheAdapter(f"sqlite+aiosqlite:///{tmp_path / 'cache.db'}")
    session_manager = SessionManager(cache_engine=adapter)
    user = MagicMock()
    user.id = "u1"
    await session_manager.add_qa(
        user_id="u1",
        question="Q",
        context="C",
        answer="A",
        session_id="s1",
        feedback_score=5,
        used_graph_element_ids={"node_ids": ["n1"], "edge_ids": ["e1"]},
    )
    graph = InMemoryGraphWithWeights()

    try:
        with (
            patch(
                "cognee.tasks.memify.extract_feedback_qas.session_user"
            ) as extract_user_ctx,
            patch(
                "cognee.tasks.memify.apply_feedback_weights.session_user"
            ) as apply_user_ctx,
            patch(
                "cognee.tasks.memify.extract_feedback_qas.get_session_manager",
                return_value=session_manager,
            ),
            patch(
                "cognee.tasks.memify.apply_feedback_weights.get_session_manager",
                return_value=session_manager,
            ),
            patch(
                "cognee.tasks.memify.apply_feedback_weights.get_graph_engine",
                return_value=graph,
            ),
        ):
            extract_user_ctx.get.return_value = user
            apply_user_ctx.get.return_value = user

            feedback_items = []
            async for item in extract_feedback_qas([{}], session_ids=["s1"]):
                feedback_items.append(item)

            result = await apply_feedback_weights(feedback_items, alpha=1.0)
    finally:
        await adapter.close()

    ranking_graph = CogneeGraph()
    close_low_feedback = add_ranked_edge(
        ranking_graph,
        "close-low-feedback",
        distance=0.1,
        feedback_weight=0.0,
    )
    far_high_feedback = add_ranked_edge(
        ranking_graph,
        "far-high-feedback",
        distance=0.2,
        feedback_weight=graph.edge_weights["e1"],
    )

    without_feedback = await ranking_graph.calculate_top_triplet_importances(
        2, feedback_influence=0.0
    )
    with_feedback = await ranking_graph.calculate_top_triplet_importances(
        2, feedback_influence=1.0
    )

    assert len(feedback_items) == 1
    assert result["applied"] == 1
    assert graph.node_weights["n1"] == pytest.approx(1.0)
    assert graph.edge_weights["e1"] == pytest.approx(1.0)
    assert without_feedback[0] == close_low_feedback
    assert with_feedback[0] == far_high_feedback
