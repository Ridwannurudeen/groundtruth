from __future__ import annotations

import os
import shutil
from dataclasses import replace
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
LOCAL_RUNTIME_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", str(ROOT))) / "GroundTruth" / "cognee"
)
QUOTA_ERROR_MARKERS = (
    "429",
    "quota",
    "rate limit",
    "rate_limit",
    "resourceexhausted",
    "too many requests",
    "exceeded your current quota",
)


def configure_runtime() -> None:
    load_dotenv(ROOT / ".env", override=True)

    os.environ.setdefault("DATA_ROOT_DIRECTORY", str(LOCAL_RUNTIME_ROOT / "data"))
    os.environ.setdefault("SYSTEM_ROOT_DIRECTORY", str(LOCAL_RUNTIME_ROOT / "system"))
    os.environ.setdefault("CACHE_ROOT_DIRECTORY", str(LOCAL_RUNTIME_ROOT / "cache"))
    os.environ.setdefault("COGNEE_LOGS_DIR", str(ROOT / ".cognee_logs"))
    os.environ.setdefault("FASTEMBED_CACHE_PATH", str(ROOT / ".fastembed_cache"))
    os.environ.setdefault("GRAPH_DATABASE_PROVIDER", "ladybug")
    os.environ.setdefault("VECTOR_DB_PROVIDER", "lancedb")
    os.environ.setdefault("DB_PROVIDER", "sqlite")

    configure_fastembed_url_fallback()
    configure_gemini_quota_fallback()


def configure_fastembed_url_fallback() -> None:
    if os.environ.get("EMBEDDING_PROVIDER") != "fastembed":
        return

    original_model = os.environ.get("EMBEDDING_MODEL")
    fallback_model = "BAAI/bge-small-en"
    if original_model == "BAAI/bge-small-en-v1.5":
        os.environ["EMBEDDING_MODEL"] = fallback_model
        os.environ["EMBEDDING_DIMENSIONS"] = "384"
        os.environ["GROUNDTRUTH_EMBEDDING_FALLBACK_FROM"] = original_model

    if os.environ.get("EMBEDDING_MODEL") != fallback_model:
        return

    from fastembed.common.model_description import ModelSource
    from fastembed.text import onnx_embedding

    for index, model in enumerate(onnx_embedding.supported_onnx_models):
        if model.model == fallback_model:
            onnx_embedding.supported_onnx_models[index] = replace(
                model,
                sources=ModelSource(
                    hf=None,
                    url="https://storage.googleapis.com/qdrant-fastembed/BAAI-bge-small-en.tar.gz",
                    _deprecated_tar_struct=True,
                ),
            )
            os.environ["GROUNDTRUTH_FASTEMBED_URL_PATCHED"] = "true"
            return


def configure_gemini_quota_fallback() -> None:
    if os.environ.get("LLM_PROVIDER") != "gemini":
        return

    original_model = os.environ.get("LLM_MODEL")
    fallback_model = "gemini/gemini-2.5-flash-lite"
    if original_model == "gemini/gemini-2.5-flash":
        os.environ["LLM_MODEL"] = fallback_model
        os.environ["GROUNDTRUTH_LLM_FALLBACK_FROM"] = original_model

    os.environ["LLM_RATE_LIMIT_ENABLED"] = "true"
    configured_requests = int(os.environ.get("LLM_RATE_LIMIT_REQUESTS") or "8")
    os.environ["LLM_RATE_LIMIT_REQUESTS"] = str(min(configured_requests, 8))
    os.environ.setdefault("LLM_RATE_LIMIT_INTERVAL", "60")


def clear_cognee_config_caches() -> None:
    from cognee.infrastructure.databases.vector.embeddings.config import get_embedding_config
    from cognee.infrastructure.databases.vector.embeddings.get_embedding_engine import (
        create_embedding_engine,
    )
    from cognee.infrastructure.llm import get_llm_config

    get_embedding_config.cache_clear()
    create_embedding_engine.cache_clear()
    get_llm_config.cache_clear()


def is_quota_error(error: BaseException) -> bool:
    text = f"{type(error).__name__}: {error}".lower()
    return any(marker in text for marker in QUOTA_ERROR_MARKERS)


def import_cognee() -> Any:
    configure_runtime()
    import cognee

    configure_runtime()
    clear_cognee_config_caches()
    return cognee


def reset_runtime_dirs() -> list[str]:
    removed = []
    for env_key in ["SYSTEM_ROOT_DIRECTORY", "DATA_ROOT_DIRECTORY", "CACHE_ROOT_DIRECTORY"]:
        path = Path(os.environ[env_key])
        if path.exists():
            shutil.rmtree(path)
            removed.append(str(path))
    return removed


configure_runtime()
