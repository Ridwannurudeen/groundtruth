# GroundTruth V3 P4 Results

Generated: 2026-07-04T23:22:32.004156+00:00
Status: `complete_deterministic_registry`

## Gate

- Time travel is deterministic over registry `state_history`; no Cognee/provider calls are used.
- `answer_as_of` filters references by state at the requested date and includes each cited claim's state chain.
- `/timeline?from=X&to=Y` exposes added / contested / revised / purged belief changes.

## Command

```powershell
.\.venv\Scripts\python.exe -m groundtruth.timeline --results-v3-p4
```

## Answer Then

```text
As of 2023-01-01T00:00:00+00:00, groundtruth_memory cites an active remembered source for 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine.
```

## Answer Now

```text
As of 2026-07-04T00:00:00+00:00, groundtruth_memory no longer cites the original retracted claim for 10.1056/nejmoa2023386. The active memory cites the retraction notice instead.
```

## Added

- `C006` `None` -> `active` / DOI `10.1016/j.adaj.2024.12.004`
  - Evidence: `user_assertion` `10.1016/j.adaj.2024.12.004`
  - Basis: Seed corpus imported this claim as an active memory claim.

- `C009` `None` -> `active` / DOI `10.1016/j.jacl.2025.04.092`
  - Evidence: `user_assertion` `10.1016/j.jacl.2025.04.092`
  - Basis: Seed corpus imported this claim as an active memory claim.

- `C010` `None` -> `active` / DOI `10.54393/df.v6i2.187`
  - Evidence: `user_assertion` `10.54393/df.v6i2.187`
  - Basis: Seed corpus imported this claim as an active memory claim.

- `C011` `None` -> `active` / DOI `10.1177/03000605261443077`
  - Evidence: `user_assertion` `10.1177/03000605261443077`
  - Basis: Seed corpus imported this claim as an active memory claim.

- `C012` `None` -> `active` / DOI `10.1001/jama.2024.1907`
  - Evidence: `user_assertion` `10.1001/jama.2024.1907`
  - Basis: Seed corpus imported this claim as an active memory claim.

- `C015` `None` -> `active` / DOI `10.3390/children12121664`
  - Evidence: `user_assertion` `10.3390/children12121664`
  - Basis: Seed corpus imported this claim as an active memory claim.

- `R002` `None` -> `retracted` / DOI `10.1016/j.heliyon.2024.e30453`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44253`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44253 supersedes original DOI 10.1016/j.heliyon.2024.e30453; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R003` `None` -> `retracted` / DOI `10.1002/bcp.70249`
  - Evidence: `authority_feed` `10.1002/bcp.70475`
  - Basis: Retraction Watch record 10.1002/bcp.70475 supersedes original DOI 10.1002/bcp.70249; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;

- `R004` `None` -> `retracted` / DOI `10.1038/s41598-025-96541-2`
  - Evidence: `authority_feed` `10.1038/s41598-026-55044-4`
  - Basis: Retraction Watch record 10.1038/s41598-026-55044-4 supersedes original DOI 10.1038/s41598-025-96541-2; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R008` `None` -> `retracted` / DOI `10.1016/j.heliyon.2024.e29871`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44378`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44378 supersedes original DOI 10.1016/j.heliyon.2024.e29871; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R010` `None` -> `retracted` / DOI `10.1007/s00500-023-09589-5`
  - Evidence: `authority_feed` `10.1007/s00500-025-11084-y`
  - Basis: Retraction Watch record 10.1007/s00500-025-11084-y supersedes original DOI 10.1007/s00500-023-09589-5; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;

- `R014` `None` -> `retracted` / DOI `10.1016/j.jacadv.2025.101686`
  - Evidence: `authority_feed` `10.1016/j.jacadv.2025.101686`
  - Basis: Retraction Watch record 10.1016/j.jacadv.2025.101686 supersedes original DOI 10.1016/j.jacadv.2025.101686; reason: Concerns/Issues about Methods;Unreliable Data;Upgrade/Update of Prior Notice(s);

- `R015` `None` -> `retracted` / DOI `10.1016/j.heliyon.2025.e41964`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2026.e44613`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R018` `None` -> `retracted` / DOI `10.1016/j.heliyon.2024.e37293`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2026.e44757`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;

## Contested

- None.

## Revised

- `R001` `active` -> `retracted` / DOI `10.1056/nejmoa2023386`
  - Evidence: `authority_feed` `10.1056/nejme2608684`
  - Basis: Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);

- `R005` `active` -> `retracted` / DOI `10.1016/j.heliyon.2023.e19675`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44379`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44379 supersedes original DOI 10.1016/j.heliyon.2023.e19675; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R006` `active` -> `retracted` / DOI `10.1371/journal.pone.0255392`
  - Evidence: `authority_feed` `10.1371/journal.pone.0349829`
  - Basis: Retraction Watch record 10.1371/journal.pone.0349829 supersedes original DOI 10.1371/journal.pone.0255392; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;

- `R007` `active` -> `retracted` / DOI `10.1016/j.heliyon.2023.e20232`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44382`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44382 supersedes original DOI 10.1016/j.heliyon.2023.e20232; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R009` `active` -> `retracted` / DOI `10.1016/j.heliyon.2023.e21222`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44400`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44400 supersedes original DOI 10.1016/j.heliyon.2023.e21222; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R011` `active` -> `retracted` / DOI `10.1007/s00500-023-09482-1`
  - Evidence: `authority_feed` `10.1007/s00500-025-11095-9`
  - Basis: Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R012` `active` -> `retracted` / DOI `10.1007/978-3-030-00524-5_6`
  - Evidence: `authority_feed` `xx10.1007/978-3-030-00524-5_9`
  - Basis: Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;

- `R013` `active` -> `retracted` / DOI `10.1007/978-3-030-00524-5_7`
  - Evidence: `authority_feed` `x10.1007/978-3-030-00524-5_9`
  - Basis: Retraction Watch record x10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_7; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;

- `R016` `active` -> `retracted` / DOI `10.1016/j.heliyon.2022.e10071`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2026.e44645`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2026.e44645 supersedes original DOI 10.1016/j.heliyon.2022.e10071; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R017` `active` -> `retracted` / DOI `10.3389/fnut.2022.803913`
  - Evidence: `authority_feed` `10.3389/fnut.2024.1520555`
  - Basis: Retraction Watch record 10.3389/fnut.2024.1520555 supersedes original DOI 10.3389/fnut.2022.803913; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;

- `R019` `active` -> `retracted` / DOI `10.1016/j.jogc.2023.102264`
  - Evidence: `authority_feed` `10.1016/j.jogc.2023.102264`
  - Basis: Retraction Watch record 10.1016/j.jogc.2023.102264 supersedes original DOI 10.1016/j.jogc.2023.102264; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;

- `R020` `active` -> `retracted` / DOI `10.1007/s00500-021-06668-3`
  - Evidence: `authority_feed` `10.1007/s00500-026-11208-y`
  - Basis: Retraction Watch record 10.1007/s00500-026-11208-y supersedes original DOI 10.1007/s00500-021-06668-3; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;

- `R022` `active` -> `retracted` / DOI `10.1080/14767058.2020.1814239`
  - Evidence: `authority_feed` `10.1080/14767058.2025.2501451`
  - Basis: Retraction Watch record 10.1080/14767058.2025.2501451 supersedes original DOI 10.1080/14767058.2020.1814239; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;

- `R023` `active` -> `retracted` / DOI `10.1080/14767058.2019.1678132`
  - Evidence: `authority_feed` `10.1080/14767058.2026.2607752`
  - Basis: Retraction Watch record 10.1080/14767058.2026.2607752 supersedes original DOI 10.1080/14767058.2019.1678132; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;

- `R024` `active` -> `retracted` / DOI `10.1080/14767058.2018.1491030`
  - Evidence: `authority_feed` `10.1080/14767058.2026.2654284`
  - Basis: Retraction Watch record 10.1080/14767058.2026.2654284 supersedes original DOI 10.1080/14767058.2018.1491030; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);

- `R025` `active` -> `retracted` / DOI `10.3109/14767058.2016.1154526`
  - Evidence: `authority_feed` `10.1080/14767058.2026.2654275`
  - Basis: Retraction Watch record 10.1080/14767058.2026.2654275 supersedes original DOI 10.3109/14767058.2016.1154526; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);

## Purged

- `R001` `active` -> `retracted` / DOI `10.1056/nejmoa2023386`
  - Evidence: `authority_feed` `10.1056/nejme2608684`
  - Basis: Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);

- `R002` `None` -> `retracted` / DOI `10.1016/j.heliyon.2024.e30453`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44253`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44253 supersedes original DOI 10.1016/j.heliyon.2024.e30453; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R003` `None` -> `retracted` / DOI `10.1002/bcp.70249`
  - Evidence: `authority_feed` `10.1002/bcp.70475`
  - Basis: Retraction Watch record 10.1002/bcp.70475 supersedes original DOI 10.1002/bcp.70249; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;

- `R004` `None` -> `retracted` / DOI `10.1038/s41598-025-96541-2`
  - Evidence: `authority_feed` `10.1038/s41598-026-55044-4`
  - Basis: Retraction Watch record 10.1038/s41598-026-55044-4 supersedes original DOI 10.1038/s41598-025-96541-2; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R005` `active` -> `retracted` / DOI `10.1016/j.heliyon.2023.e19675`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44379`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44379 supersedes original DOI 10.1016/j.heliyon.2023.e19675; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R006` `active` -> `retracted` / DOI `10.1371/journal.pone.0255392`
  - Evidence: `authority_feed` `10.1371/journal.pone.0349829`
  - Basis: Retraction Watch record 10.1371/journal.pone.0349829 supersedes original DOI 10.1371/journal.pone.0255392; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;

- `R007` `active` -> `retracted` / DOI `10.1016/j.heliyon.2023.e20232`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44382`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44382 supersedes original DOI 10.1016/j.heliyon.2023.e20232; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R008` `None` -> `retracted` / DOI `10.1016/j.heliyon.2024.e29871`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44378`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44378 supersedes original DOI 10.1016/j.heliyon.2024.e29871; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R009` `active` -> `retracted` / DOI `10.1016/j.heliyon.2023.e21222`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2025.e44400`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2025.e44400 supersedes original DOI 10.1016/j.heliyon.2023.e21222; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R010` `None` -> `retracted` / DOI `10.1007/s00500-023-09589-5`
  - Evidence: `authority_feed` `10.1007/s00500-025-11084-y`
  - Basis: Retraction Watch record 10.1007/s00500-025-11084-y supersedes original DOI 10.1007/s00500-023-09589-5; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;

- `R011` `active` -> `retracted` / DOI `10.1007/s00500-023-09482-1`
  - Evidence: `authority_feed` `10.1007/s00500-025-11095-9`
  - Basis: Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R012` `active` -> `retracted` / DOI `10.1007/978-3-030-00524-5_6`
  - Evidence: `authority_feed` `xx10.1007/978-3-030-00524-5_9`
  - Basis: Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;

- `R013` `active` -> `retracted` / DOI `10.1007/978-3-030-00524-5_7`
  - Evidence: `authority_feed` `x10.1007/978-3-030-00524-5_9`
  - Basis: Retraction Watch record x10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_7; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;

- `R014` `None` -> `retracted` / DOI `10.1016/j.jacadv.2025.101686`
  - Evidence: `authority_feed` `10.1016/j.jacadv.2025.101686`
  - Basis: Retraction Watch record 10.1016/j.jacadv.2025.101686 supersedes original DOI 10.1016/j.jacadv.2025.101686; reason: Concerns/Issues about Methods;Unreliable Data;Upgrade/Update of Prior Notice(s);

- `R015` `None` -> `retracted` / DOI `10.1016/j.heliyon.2025.e41964`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2026.e44613`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R016` `active` -> `retracted` / DOI `10.1016/j.heliyon.2022.e10071`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2026.e44645`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2026.e44645 supersedes original DOI 10.1016/j.heliyon.2022.e10071; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;

- `R017` `active` -> `retracted` / DOI `10.3389/fnut.2022.803913`
  - Evidence: `authority_feed` `10.3389/fnut.2024.1520555`
  - Basis: Retraction Watch record 10.3389/fnut.2024.1520555 supersedes original DOI 10.3389/fnut.2022.803913; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;

- `R018` `None` -> `retracted` / DOI `10.1016/j.heliyon.2024.e37293`
  - Evidence: `authority_feed` `10.1016/j.heliyon.2026.e44757`
  - Basis: Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;

- `R019` `active` -> `retracted` / DOI `10.1016/j.jogc.2023.102264`
  - Evidence: `authority_feed` `10.1016/j.jogc.2023.102264`
  - Basis: Retraction Watch record 10.1016/j.jogc.2023.102264 supersedes original DOI 10.1016/j.jogc.2023.102264; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;

- `R020` `active` -> `retracted` / DOI `10.1007/s00500-021-06668-3`
  - Evidence: `authority_feed` `10.1007/s00500-026-11208-y`
  - Basis: Retraction Watch record 10.1007/s00500-026-11208-y supersedes original DOI 10.1007/s00500-021-06668-3; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;

- `R022` `active` -> `retracted` / DOI `10.1080/14767058.2020.1814239`
  - Evidence: `authority_feed` `10.1080/14767058.2025.2501451`
  - Basis: Retraction Watch record 10.1080/14767058.2025.2501451 supersedes original DOI 10.1080/14767058.2020.1814239; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;

- `R023` `active` -> `retracted` / DOI `10.1080/14767058.2019.1678132`
  - Evidence: `authority_feed` `10.1080/14767058.2026.2607752`
  - Basis: Retraction Watch record 10.1080/14767058.2026.2607752 supersedes original DOI 10.1080/14767058.2019.1678132; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;

- `R024` `active` -> `retracted` / DOI `10.1080/14767058.2018.1491030`
  - Evidence: `authority_feed` `10.1080/14767058.2026.2654284`
  - Basis: Retraction Watch record 10.1080/14767058.2026.2654284 supersedes original DOI 10.1080/14767058.2018.1491030; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);

- `R025` `active` -> `retracted` / DOI `10.3109/14767058.2016.1154526`
  - Evidence: `authority_feed` `10.1080/14767058.2026.2654275`
  - Basis: Retraction Watch record 10.1080/14767058.2026.2654275 supersedes original DOI 10.3109/14767058.2016.1154526; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);

## Raw Run

```json
{
  "after": {
    "as_of": "2026-07-04T00:00:00+00:00",
    "chains": [
      {
        "claim_id": "R001",
        "state_history": [
          {
            "at": "2021-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1056/nejmoa2023386",
            "state": "active"
          },
          {
            "at": "2026-06-29T00:00:00+00:00",
            "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
            "evidence_class": "authority_feed",
            "evidence_ref": "10.1056/nejme2608684",
            "state": "retracted"
          }
        ]
      },
      {
        "claim_id": "R011",
        "state_history": [
          {
            "at": "2023-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1007/s00500-023-09482-1",
            "state": "active"
          },
          {
            "at": "2025-12-31T00:00:00+00:00",
            "basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
            "evidence_class": "authority_feed",
            "evidence_ref": "10.1007/s00500-025-11095-9",
            "state": "retracted"
          }
        ]
      },
      {
        "claim_id": "R012",
        "state_history": [
          {
            "at": "2019-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1007/978-3-030-00524-5_6",
            "state": "active"
          },
          {
            "at": "2024-10-15T00:00:00+00:00",
            "basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
            "evidence_class": "authority_feed",
            "evidence_ref": "xx10.1007/978-3-030-00524-5_9",
            "state": "retracted"
          }
        ]
      },
      {
        "claim_id": "R015",
        "state_history": [
          {
            "at": "2025-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1016/j.heliyon.2025.e41964",
            "state": "active"
          },
          {
            "at": "2026-02-11T00:00:00+00:00",
            "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
            "evidence_class": "authority_feed",
            "evidence_ref": "10.1016/j.heliyon.2026.e44613",
            "state": "retracted"
          }
        ]
      },
      {
        "claim_id": "R018",
        "state_history": [
          {
            "at": "2024-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1016/j.heliyon.2024.e37293",
            "state": "active"
          },
          {
            "at": "2026-03-17T00:00:00+00:00",
            "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
            "evidence_class": "authority_feed",
            "evidence_ref": "10.1016/j.heliyon.2026.e44757",
            "state": "retracted"
          }
        ]
      }
    ],
    "cites_by_state": {
      "active": 0,
      "contested": 0,
      "purged": 0,
      "retracted": 5,
      "superseded": 0
    },
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "eligible_claims": 40,
    "question": "What did we believe about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
    "recall_mode": "deterministic_registry_time_travel",
    "references": [
      {
        "belief_evidence_class": "authority_feed",
        "belief_evidence_ref": "10.1056/nejme2608684",
        "belief_state": "retracted",
        "belief_state_basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
        "belief_state_changed_at": "2026-06-29T00:00:00+00:00",
        "claim_id": "R001",
        "cohort": "retracted_original",
        "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1056/nejmoa2023386",
        "kind": "retraction_notice",
        "latest_basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
        "latest_state_change": {
          "at": "2026-06-29T00:00:00+00:00",
          "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1056/nejme2608684",
          "state": "retracted"
        },
        "retracted": false,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "authority_feed",
        "belief_evidence_ref": "10.1007/s00500-025-11095-9",
        "belief_state": "retracted",
        "belief_state_basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "belief_state_changed_at": "2025-12-31T00:00:00+00:00",
        "claim_id": "R011",
        "cohort": "retracted_original",
        "data_id": "7ee50471-5eca-5da5-9a46-98f60e8c6d87",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1007/s00500-023-09482-1",
        "kind": "retraction_notice",
        "latest_basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "latest_state_change": {
          "at": "2025-12-31T00:00:00+00:00",
          "basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-025-11095-9",
          "state": "retracted"
        },
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "authority_feed",
        "belief_evidence_ref": "xx10.1007/978-3-030-00524-5_9",
        "belief_state": "retracted",
        "belief_state_basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
        "belief_state_changed_at": "2024-10-15T00:00:00+00:00",
        "claim_id": "R012",
        "cohort": "retracted_original",
        "data_id": "7de422b8-8606-50c3-951a-17a00330ff96",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1007/978-3-030-00524-5_6",
        "kind": "retraction_notice",
        "latest_basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
        "latest_state_change": {
          "at": "2024-10-15T00:00:00+00:00",
          "basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "evidence_class": "authority_feed",
          "evidence_ref": "xx10.1007/978-3-030-00524-5_9",
          "state": "retracted"
        },
        "retracted": false,
        "score": 1,
        "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "authority_feed",
        "belief_evidence_ref": "10.1016/j.heliyon.2026.e44613",
        "belief_state": "retracted",
        "belief_state_basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "belief_state_changed_at": "2026-02-11T00:00:00+00:00",
        "claim_id": "R015",
        "cohort": "retracted_original",
        "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "retraction_notice",
        "latest_basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "latest_state_change": {
          "at": "2026-02-11T00:00:00+00:00",
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44613",
          "state": "retracted"
        },
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "authority_feed",
        "belief_evidence_ref": "10.1016/j.heliyon.2026.e44757",
        "belief_state": "retracted",
        "belief_state_basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
        "belief_state_changed_at": "2026-03-17T00:00:00+00:00",
        "claim_id": "R018",
        "cohort": "retracted_original",
        "data_id": "5c55498c-b1e0-5849-a775-90619c77163b",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1016/j.heliyon.2024.e37293",
        "kind": "retraction_notice",
        "latest_basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
        "latest_state_change": {
          "at": "2026-03-17T00:00:00+00:00",
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44757",
          "state": "retracted"
        },
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "retracted_forgotten"
      }
    ],
    "retracted_dois": [],
    "text": "As of 2026-07-04T00:00:00+00:00, groundtruth_memory no longer cites the original retracted claim for 10.1056/nejmoa2023386. The active memory cites the retraction notice instead."
  },
  "before": {
    "as_of": "2023-01-01T00:00:00+00:00",
    "chains": [
      {
        "claim_id": "R001",
        "state_history": [
          {
            "at": "2021-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1056/nejmoa2023386",
            "state": "active"
          }
        ]
      },
      {
        "claim_id": "R011",
        "state_history": [
          {
            "at": "2023-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1007/s00500-023-09482-1",
            "state": "active"
          }
        ]
      },
      {
        "claim_id": "R012",
        "state_history": [
          {
            "at": "2019-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1007/978-3-030-00524-5_6",
            "state": "active"
          }
        ]
      },
      {
        "claim_id": "R020",
        "state_history": [
          {
            "at": "2022-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1007/s00500-021-06668-3",
            "state": "active"
          }
        ]
      },
      {
        "claim_id": "R022",
        "state_history": [
          {
            "at": "2020-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1080/14767058.2020.1814239",
            "state": "active"
          }
        ]
      }
    ],
    "cites_by_state": {
      "active": 5,
      "contested": 0,
      "purged": 0,
      "retracted": 0,
      "superseded": 0
    },
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "eligible_claims": 26,
    "question": "What did we believe about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
    "recall_mode": "deterministic_registry_time_travel",
    "references": [
      {
        "belief_evidence_class": "user_assertion",
        "belief_evidence_ref": "10.1056/nejmoa2023386",
        "belief_state": "active",
        "belief_state_basis": "Seed corpus imported this claim as an active memory claim.",
        "belief_state_changed_at": "2021-01-01T00:00:00+00:00",
        "claim_id": "R001",
        "cohort": "retracted_original",
        "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1056/nejmoa2023386",
        "kind": "original_claim",
        "latest_basis": "Seed corpus imported this claim as an active memory claim.",
        "latest_state_change": {
          "at": "2021-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1056/nejmoa2023386",
          "state": "active"
        },
        "retracted": false,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "user_assertion",
        "belief_evidence_ref": "10.1007/s00500-023-09482-1",
        "belief_state": "active",
        "belief_state_basis": "Seed corpus imported this claim as an active memory claim.",
        "belief_state_changed_at": "2023-01-01T00:00:00+00:00",
        "claim_id": "R011",
        "cohort": "retracted_original",
        "data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09482-1",
        "kind": "original_claim",
        "latest_basis": "Seed corpus imported this claim as an active memory claim.",
        "latest_state_change": {
          "at": "2023-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1007/s00500-023-09482-1",
          "state": "active"
        },
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "user_assertion",
        "belief_evidence_ref": "10.1007/978-3-030-00524-5_6",
        "belief_state": "active",
        "belief_state_basis": "Seed corpus imported this claim as an active memory claim.",
        "belief_state_changed_at": "2019-01-01T00:00:00+00:00",
        "claim_id": "R012",
        "cohort": "retracted_original",
        "data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/978-3-030-00524-5_6",
        "kind": "original_claim",
        "latest_basis": "Seed corpus imported this claim as an active memory claim.",
        "latest_state_change": {
          "at": "2019-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1007/978-3-030-00524-5_6",
          "state": "active"
        },
        "retracted": false,
        "score": 1,
        "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "user_assertion",
        "belief_evidence_ref": "10.1007/s00500-021-06668-3",
        "belief_state": "active",
        "belief_state_basis": "Seed corpus imported this claim as an active memory claim.",
        "belief_state_changed_at": "2022-01-01T00:00:00+00:00",
        "claim_id": "R020",
        "cohort": "retracted_original",
        "data_id": "eb56d69a-6313-5dd0-93d8-1d73c161dd3e",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/s00500-021-06668-3",
        "kind": "original_claim",
        "latest_basis": "Seed corpus imported this claim as an active memory claim.",
        "latest_state_change": {
          "at": "2022-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1007/s00500-021-06668-3",
          "state": "active"
        },
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "retracted_forgotten"
      },
      {
        "belief_evidence_class": "user_assertion",
        "belief_evidence_ref": "10.1080/14767058.2020.1814239",
        "belief_state": "active",
        "belief_state_basis": "Seed corpus imported this claim as an active memory claim.",
        "belief_state_changed_at": "2020-01-01T00:00:00+00:00",
        "claim_id": "R022",
        "cohort": "retracted_original",
        "data_id": "76a51f40-5e8e-5f6b-bb4a-5587be84fbb9",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1080/14767058.2020.1814239",
        "kind": "original_claim",
        "latest_basis": "Seed corpus imported this claim as an active memory claim.",
        "latest_state_change": {
          "at": "2020-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1080/14767058.2020.1814239",
          "state": "active"
        },
        "retracted": false,
        "score": 1,
        "source": "The Journal of Maternal-Fetal & Neonatal Medicine",
        "status": "retracted_forgotten"
      }
    ],
    "retracted_dois": [],
    "text": "As of 2023-01-01T00:00:00+00:00, groundtruth_memory cites an active remembered source for 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine."
  },
  "from": "2023-01-01T00:00:00+00:00",
  "generated_at": "2026-07-04T23:22:32.004156+00:00",
  "question": "What did we believe about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
  "timeline": {
    "changes": {
      "added": [
        {
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.adaj.2024.12.004",
              "state": "active"
            }
          ],
          "changed_at": "2025-01-01T00:00:00+00:00",
          "claim_id": "C006",
          "doi": "10.1016/j.adaj.2024.12.004",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1016/j.adaj.2024.12.004",
          "from_state": null,
          "memory_status": "active",
          "title": "Beyond sugar-sweetened beverages",
          "to_state": "active"
        },
        {
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.jacl.2025.04.092",
              "state": "active"
            }
          ],
          "changed_at": "2025-01-01T00:00:00+00:00",
          "claim_id": "C009",
          "doi": "10.1016/j.jacl.2025.04.092",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1016/j.jacl.2025.04.092",
          "from_state": null,
          "memory_status": "active",
          "title": "Lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL",
          "to_state": "active"
        },
        {
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.54393/df.v6i2.187",
              "state": "active"
            }
          ],
          "changed_at": "2025-01-01T00:00:00+00:00",
          "claim_id": "C010",
          "doi": "10.54393/df.v6i2.187",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.54393/df.v6i2.187",
          "from_state": null,
          "memory_status": "active",
          "title": "Plant-Based Diet Adherence and Type 2 Diabetes Risk Factors",
          "to_state": "active"
        },
        {
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "chain": [
            {
              "at": "2026-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1177/03000605261443077",
              "state": "active"
            }
          ],
          "changed_at": "2026-01-01T00:00:00+00:00",
          "claim_id": "C011",
          "doi": "10.1177/03000605261443077",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1177/03000605261443077",
          "from_state": null,
          "memory_status": "active",
          "title": "Effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis",
          "to_state": "active"
        },
        {
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1001/jama.2024.1907",
              "state": "active"
            }
          ],
          "changed_at": "2024-01-01T00:00:00+00:00",
          "claim_id": "C012",
          "doi": "10.1001/jama.2024.1907",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.1001/jama.2024.1907",
          "from_state": null,
          "memory_status": "active",
          "title": "Dietary Sodium and Blood Pressure",
          "to_state": "active"
        },
        {
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.3390/children12121664",
              "state": "active"
            }
          ],
          "changed_at": "2025-01-01T00:00:00+00:00",
          "claim_id": "C015",
          "doi": "10.3390/children12121664",
          "evidence_class": "user_assertion",
          "evidence_ref": "10.3390/children12121664",
          "from_state": null,
          "memory_status": "active",
          "title": "Dietary Fat and Protein Intake and Their Impact on Glycemic Control in Pediatric Type 1 Diabetes: A Narrative Review",
          "to_state": "active"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44253 supersedes original DOI 10.1016/j.heliyon.2024.e30453; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2024.e30453",
              "state": "active"
            },
            {
              "at": "2025-11-24T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44253 supersedes original DOI 10.1016/j.heliyon.2024.e30453; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44253",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-11-24T00:00:00+00:00",
          "claim_id": "R002",
          "doi": "10.1016/j.heliyon.2024.e30453",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44253",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1002/bcp.70475 supersedes original DOI 10.1002/bcp.70249; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1002/bcp.70249",
              "state": "active"
            },
            {
              "at": "2026-01-22T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1002/bcp.70475 supersedes original DOI 10.1002/bcp.70249; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1002/bcp.70475",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-01-22T00:00:00+00:00",
          "claim_id": "R003",
          "doi": "10.1002/bcp.70249",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1002/bcp.70475",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1038/s41598-026-55044-4 supersedes original DOI 10.1038/s41598-025-96541-2; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1038/s41598-025-96541-2",
              "state": "active"
            },
            {
              "at": "2026-06-03T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1038/s41598-026-55044-4 supersedes original DOI 10.1038/s41598-025-96541-2; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1038/s41598-026-55044-4",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-06-03T00:00:00+00:00",
          "claim_id": "R004",
          "doi": "10.1038/s41598-025-96541-2",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1038/s41598-026-55044-4",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "An effective PO-RSNN and FZCIS based diabetes prediction and stroke analysis in the metaverse environment",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44378 supersedes original DOI 10.1016/j.heliyon.2024.e29871; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2024.e29871",
              "state": "active"
            },
            {
              "at": "2025-12-16T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44378 supersedes original DOI 10.1016/j.heliyon.2024.e29871; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44378",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-16T00:00:00+00:00",
          "claim_id": "R008",
          "doi": "10.1016/j.heliyon.2024.e29871",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44378",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "NF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1007/s00500-025-11084-y supersedes original DOI 10.1007/s00500-023-09589-5; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/s00500-023-09589-5",
              "state": "active"
            },
            {
              "at": "2025-12-31T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1007/s00500-025-11084-y supersedes original DOI 10.1007/s00500-023-09589-5; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1007/s00500-025-11084-y",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-31T00:00:00+00:00",
          "claim_id": "R010",
          "doi": "10.1007/s00500-023-09589-5",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-025-11084-y",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Distribution characteristics of inhalable particulate pollutants and their effects on cardiopulmonary respiratory system of outdoor football players in a smart healthcare system",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.jacadv.2025.101686 supersedes original DOI 10.1016/j.jacadv.2025.101686; reason: Concerns/Issues about Methods;Unreliable Data;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.jacadv.2025.101686",
              "state": "active"
            },
            {
              "at": "2026-03-11T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.jacadv.2025.101686 supersedes original DOI 10.1016/j.jacadv.2025.101686; reason: Concerns/Issues about Methods;Unreliable Data;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.jacadv.2025.101686",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-03-11T00:00:00+00:00",
          "claim_id": "R014",
          "doi": "10.1016/j.jacadv.2025.101686",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.jacadv.2025.101686",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2025.e41964",
              "state": "active"
            },
            {
              "at": "2026-02-11T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2026.e44613",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-02-11T00:00:00+00:00",
          "claim_id": "R015",
          "doi": "10.1016/j.heliyon.2025.e41964",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44613",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2024.e37293",
              "state": "active"
            },
            {
              "at": "2026-03-17T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2026.e44757",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-03-17T00:00:00+00:00",
          "claim_id": "R018",
          "doi": "10.1016/j.heliyon.2024.e37293",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44757",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "MobileNet-V2 /IFHO model for Accurate Detection of early-stage diabetic retinopathy",
          "to_state": "retracted"
        }
      ],
      "contested": [],
      "purged": [
        {
          "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2021-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1056/nejmoa2023386",
              "state": "active"
            },
            {
              "at": "2026-06-29T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1056/nejme2608684",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-06-29T00:00:00+00:00",
          "claim_id": "R001",
          "doi": "10.1056/nejmoa2023386",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1056/nejme2608684",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Avacopan for the Treatment of ANCA-Associated Vasculitis",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44253 supersedes original DOI 10.1016/j.heliyon.2024.e30453; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2024.e30453",
              "state": "active"
            },
            {
              "at": "2025-11-24T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44253 supersedes original DOI 10.1016/j.heliyon.2024.e30453; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44253",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-11-24T00:00:00+00:00",
          "claim_id": "R002",
          "doi": "10.1016/j.heliyon.2024.e30453",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44253",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1002/bcp.70475 supersedes original DOI 10.1002/bcp.70249; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1002/bcp.70249",
              "state": "active"
            },
            {
              "at": "2026-01-22T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1002/bcp.70475 supersedes original DOI 10.1002/bcp.70249; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1002/bcp.70475",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-01-22T00:00:00+00:00",
          "claim_id": "R003",
          "doi": "10.1002/bcp.70249",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1002/bcp.70475",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1038/s41598-026-55044-4 supersedes original DOI 10.1038/s41598-025-96541-2; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1038/s41598-025-96541-2",
              "state": "active"
            },
            {
              "at": "2026-06-03T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1038/s41598-026-55044-4 supersedes original DOI 10.1038/s41598-025-96541-2; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1038/s41598-026-55044-4",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-06-03T00:00:00+00:00",
          "claim_id": "R004",
          "doi": "10.1038/s41598-025-96541-2",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1038/s41598-026-55044-4",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "An effective PO-RSNN and FZCIS based diabetes prediction and stroke analysis in the metaverse environment",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44379 supersedes original DOI 10.1016/j.heliyon.2023.e19675; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2023.e19675",
              "state": "active"
            },
            {
              "at": "2025-12-16T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44379 supersedes original DOI 10.1016/j.heliyon.2023.e19675; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44379",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-16T00:00:00+00:00",
          "claim_id": "R005",
          "doi": "10.1016/j.heliyon.2023.e19675",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44379",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "The interplay between monosodium glutamate (MSG) consumption and metabolic disorders",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1371/journal.pone.0349829 supersedes original DOI 10.1371/journal.pone.0255392; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2021-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1371/journal.pone.0255392",
              "state": "active"
            },
            {
              "at": "2026-05-21T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1371/journal.pone.0349829 supersedes original DOI 10.1371/journal.pone.0255392; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1371/journal.pone.0349829",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-05-21T00:00:00+00:00",
          "claim_id": "R006",
          "doi": "10.1371/journal.pone.0255392",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1371/journal.pone.0349829",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Food insecurity and mental health of women during COVID-19: Evidence from a developing country",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44382 supersedes original DOI 10.1016/j.heliyon.2023.e20232; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2023.e20232",
              "state": "active"
            },
            {
              "at": "2025-12-16T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44382 supersedes original DOI 10.1016/j.heliyon.2023.e20232; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44382",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-16T00:00:00+00:00",
          "claim_id": "R007",
          "doi": "10.1016/j.heliyon.2023.e20232",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44382",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44378 supersedes original DOI 10.1016/j.heliyon.2024.e29871; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2024.e29871",
              "state": "active"
            },
            {
              "at": "2025-12-16T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44378 supersedes original DOI 10.1016/j.heliyon.2024.e29871; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44378",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-16T00:00:00+00:00",
          "claim_id": "R008",
          "doi": "10.1016/j.heliyon.2024.e29871",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44378",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "NF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44400 supersedes original DOI 10.1016/j.heliyon.2023.e21222; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2023.e21222",
              "state": "active"
            },
            {
              "at": "2025-12-21T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44400 supersedes original DOI 10.1016/j.heliyon.2023.e21222; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44400",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-21T00:00:00+00:00",
          "claim_id": "R009",
          "doi": "10.1016/j.heliyon.2023.e21222",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44400",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Fenchone and camphor: Main natural compounds from Lavandula stoechas L., expediting multiple in vitro biological activities",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1007/s00500-025-11084-y supersedes original DOI 10.1007/s00500-023-09589-5; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/s00500-023-09589-5",
              "state": "active"
            },
            {
              "at": "2025-12-31T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1007/s00500-025-11084-y supersedes original DOI 10.1007/s00500-023-09589-5; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1007/s00500-025-11084-y",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-31T00:00:00+00:00",
          "claim_id": "R010",
          "doi": "10.1007/s00500-023-09589-5",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-025-11084-y",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Distribution characteristics of inhalable particulate pollutants and their effects on cardiopulmonary respiratory system of outdoor football players in a smart healthcare system",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/s00500-023-09482-1",
              "state": "active"
            },
            {
              "at": "2025-12-31T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1007/s00500-025-11095-9",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-31T00:00:00+00:00",
          "claim_id": "R011",
          "doi": "10.1007/s00500-023-09482-1",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-025-11095-9",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "An attention-based dense network model for cardiac image segmentation using learning approaches",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2019-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/978-3-030-00524-5_6",
              "state": "active"
            },
            {
              "at": "2024-10-15T00:00:00+00:00",
              "basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "xx10.1007/978-3-030-00524-5_9",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-10-15T00:00:00+00:00",
          "claim_id": "R012",
          "doi": "10.1007/978-3-030-00524-5_6",
          "evidence_class": "authority_feed",
          "evidence_ref": "xx10.1007/978-3-030-00524-5_9",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "SiloMAS: A MAS for Smart Silos to Optimize Food and Water Consumption on Livestock Holdings",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record x10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_7; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2019-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/978-3-030-00524-5_7",
              "state": "active"
            },
            {
              "at": "2024-10-15T00:00:00+00:00",
              "basis": "Retraction Watch record x10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_7; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "x10.1007/978-3-030-00524-5_9",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-10-15T00:00:00+00:00",
          "claim_id": "R013",
          "doi": "10.1007/978-3-030-00524-5_7",
          "evidence_class": "authority_feed",
          "evidence_ref": "x10.1007/978-3-030-00524-5_9",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Intelligent Livestock Feeding System by Means of Silos with IoT Technology",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.jacadv.2025.101686 supersedes original DOI 10.1016/j.jacadv.2025.101686; reason: Concerns/Issues about Methods;Unreliable Data;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.jacadv.2025.101686",
              "state": "active"
            },
            {
              "at": "2026-03-11T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.jacadv.2025.101686 supersedes original DOI 10.1016/j.jacadv.2025.101686; reason: Concerns/Issues about Methods;Unreliable Data;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.jacadv.2025.101686",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-03-11T00:00:00+00:00",
          "claim_id": "R014",
          "doi": "10.1016/j.jacadv.2025.101686",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.jacadv.2025.101686",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2025-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2025.e41964",
              "state": "active"
            },
            {
              "at": "2026-02-11T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44613 supersedes original DOI 10.1016/j.heliyon.2025.e41964; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2026.e44613",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-02-11T00:00:00+00:00",
          "claim_id": "R015",
          "doi": "10.1016/j.heliyon.2025.e41964",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44613",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "Targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44645 supersedes original DOI 10.1016/j.heliyon.2022.e10071; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2022-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2022.e10071",
              "state": "active"
            },
            {
              "at": "2026-02-26T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44645 supersedes original DOI 10.1016/j.heliyon.2022.e10071; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2026.e44645",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-02-26T00:00:00+00:00",
          "claim_id": "R016",
          "doi": "10.1016/j.heliyon.2022.e10071",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44645",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.3389/fnut.2024.1520555 supersedes original DOI 10.3389/fnut.2022.803913; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;",
          "chain": [
            {
              "at": "2022-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.3389/fnut.2022.803913",
              "state": "active"
            },
            {
              "at": "2024-11-05T00:00:00+00:00",
              "basis": "Retraction Watch record 10.3389/fnut.2024.1520555 supersedes original DOI 10.3389/fnut.2022.803913; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.3389/fnut.2024.1520555",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-11-05T00:00:00+00:00",
          "claim_id": "R017",
          "doi": "10.3389/fnut.2022.803913",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.3389/fnut.2024.1520555",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2024-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2024.e37293",
              "state": "active"
            },
            {
              "at": "2026-03-17T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44757 supersedes original DOI 10.1016/j.heliyon.2024.e37293; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2026.e44757",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-03-17T00:00:00+00:00",
          "claim_id": "R018",
          "doi": "10.1016/j.heliyon.2024.e37293",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44757",
          "from_state": null,
          "memory_status": "retracted_forgotten",
          "title": "MobileNet-V2 /IFHO model for Accurate Detection of early-stage diabetic retinopathy",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.jogc.2023.102264 supersedes original DOI 10.1016/j.jogc.2023.102264; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.jogc.2023.102264",
              "state": "active"
            },
            {
              "at": "2024-09-26T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.jogc.2023.102264 supersedes original DOI 10.1016/j.jogc.2023.102264; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.jogc.2023.102264",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-09-26T00:00:00+00:00",
          "claim_id": "R019",
          "doi": "10.1016/j.jogc.2023.102264",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.jogc.2023.102264",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "The Effect of Preoperative Intravenous Tranexamic Acid Versus Rectal Misoprostol in Reducing Blood Loss During and After Elective Cesarean Delivery in Primigravida: A Double-Blinded, Randomized, Comparative-Placebo Trial",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1007/s00500-026-11208-y supersedes original DOI 10.1007/s00500-021-06668-3; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2022-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/s00500-021-06668-3",
              "state": "active"
            },
            {
              "at": "2026-01-21T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1007/s00500-026-11208-y supersedes original DOI 10.1007/s00500-021-06668-3; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1007/s00500-026-11208-y",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-01-21T00:00:00+00:00",
          "claim_id": "R020",
          "doi": "10.1007/s00500-021-06668-3",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-026-11208-y",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Fat-based studies for computer-assisted screening of child obesity using thermal imaging based on deep learning techniques: a comparison with quantum machine learning approach",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2025.2501451 supersedes original DOI 10.1080/14767058.2020.1814239; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2020-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1080/14767058.2020.1814239",
              "state": "active"
            },
            {
              "at": "2025-05-08T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2025.2501451 supersedes original DOI 10.1080/14767058.2020.1814239; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2025.2501451",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-05-08T00:00:00+00:00",
          "claim_id": "R022",
          "doi": "10.1080/14767058.2020.1814239",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2025.2501451",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Omega-3 fatty acids plus vitamin for women with gestational diabetes or prediabetes: a meta-analysis of randomized controlled studies",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2026.2607752 supersedes original DOI 10.1080/14767058.2019.1678132; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2020-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1080/14767058.2019.1678132",
              "state": "active"
            },
            {
              "at": "2026-01-07T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2026.2607752 supersedes original DOI 10.1080/14767058.2019.1678132; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2026.2607752",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-01-07T00:00:00+00:00",
          "claim_id": "R023",
          "doi": "10.1080/14767058.2019.1678132",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2026.2607752",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Ultrasound markers for prediction of gestational diabetes mellitus in early pregnancy in Egyptian women: observational study",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2026.2654284 supersedes original DOI 10.1080/14767058.2018.1491030; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2018-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1080/14767058.2018.1491030",
              "state": "active"
            },
            {
              "at": "2026-04-07T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2026.2654284 supersedes original DOI 10.1080/14767058.2018.1491030; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2026.2654284",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-04-07T00:00:00+00:00",
          "claim_id": "R024",
          "doi": "10.1080/14767058.2018.1491030",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2026.2654284",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Maternal, fetal, and neonatal outcomes among different types of hypertensive disorders associating pregnancy needing intensive care management",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2026.2654275 supersedes original DOI 10.3109/14767058.2016.1154526; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2016-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.3109/14767058.2016.1154526",
              "state": "active"
            },
            {
              "at": "2026-04-09T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2026.2654275 supersedes original DOI 10.3109/14767058.2016.1154526; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2026.2654275",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-04-09T00:00:00+00:00",
          "claim_id": "R025",
          "doi": "10.3109/14767058.2016.1154526",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2026.2654275",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial",
          "to_state": "retracted"
        }
      ],
      "revised": [
        {
          "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2021-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1056/nejmoa2023386",
              "state": "active"
            },
            {
              "at": "2026-06-29T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1056/nejme2608684",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-06-29T00:00:00+00:00",
          "claim_id": "R001",
          "doi": "10.1056/nejmoa2023386",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1056/nejme2608684",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Avacopan for the Treatment of ANCA-Associated Vasculitis",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44379 supersedes original DOI 10.1016/j.heliyon.2023.e19675; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2023.e19675",
              "state": "active"
            },
            {
              "at": "2025-12-16T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44379 supersedes original DOI 10.1016/j.heliyon.2023.e19675; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44379",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-16T00:00:00+00:00",
          "claim_id": "R005",
          "doi": "10.1016/j.heliyon.2023.e19675",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44379",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "The interplay between monosodium glutamate (MSG) consumption and metabolic disorders",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1371/journal.pone.0349829 supersedes original DOI 10.1371/journal.pone.0255392; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2021-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1371/journal.pone.0255392",
              "state": "active"
            },
            {
              "at": "2026-05-21T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1371/journal.pone.0349829 supersedes original DOI 10.1371/journal.pone.0255392; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1371/journal.pone.0349829",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-05-21T00:00:00+00:00",
          "claim_id": "R006",
          "doi": "10.1371/journal.pone.0255392",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1371/journal.pone.0349829",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Food insecurity and mental health of women during COVID-19: Evidence from a developing country",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44382 supersedes original DOI 10.1016/j.heliyon.2023.e20232; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2023.e20232",
              "state": "active"
            },
            {
              "at": "2025-12-16T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44382 supersedes original DOI 10.1016/j.heliyon.2023.e20232; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44382",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-16T00:00:00+00:00",
          "claim_id": "R007",
          "doi": "10.1016/j.heliyon.2023.e20232",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44382",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44400 supersedes original DOI 10.1016/j.heliyon.2023.e21222; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2023.e21222",
              "state": "active"
            },
            {
              "at": "2025-12-21T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2025.e44400 supersedes original DOI 10.1016/j.heliyon.2023.e21222; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2025.e44400",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-21T00:00:00+00:00",
          "claim_id": "R009",
          "doi": "10.1016/j.heliyon.2023.e21222",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2025.e44400",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Fenchone and camphor: Main natural compounds from Lavandula stoechas L., expediting multiple in vitro biological activities",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/s00500-023-09482-1",
              "state": "active"
            },
            {
              "at": "2025-12-31T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1007/s00500-025-11095-9 supersedes original DOI 10.1007/s00500-023-09482-1; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1007/s00500-025-11095-9",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-12-31T00:00:00+00:00",
          "claim_id": "R011",
          "doi": "10.1007/s00500-023-09482-1",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-025-11095-9",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "An attention-based dense network model for cardiac image segmentation using learning approaches",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2019-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/978-3-030-00524-5_6",
              "state": "active"
            },
            {
              "at": "2024-10-15T00:00:00+00:00",
              "basis": "Retraction Watch record xx10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_6; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "xx10.1007/978-3-030-00524-5_9",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-10-15T00:00:00+00:00",
          "claim_id": "R012",
          "doi": "10.1007/978-3-030-00524-5_6",
          "evidence_class": "authority_feed",
          "evidence_ref": "xx10.1007/978-3-030-00524-5_9",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "SiloMAS: A MAS for Smart Silos to Optimize Food and Water Consumption on Livestock Holdings",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record x10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_7; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2019-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/978-3-030-00524-5_7",
              "state": "active"
            },
            {
              "at": "2024-10-15T00:00:00+00:00",
              "basis": "Retraction Watch record x10.1007/978-3-030-00524-5_9 supersedes original DOI 10.1007/978-3-030-00524-5_7; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "x10.1007/978-3-030-00524-5_9",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-10-15T00:00:00+00:00",
          "claim_id": "R013",
          "doi": "10.1007/978-3-030-00524-5_7",
          "evidence_class": "authority_feed",
          "evidence_ref": "x10.1007/978-3-030-00524-5_9",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Intelligent Livestock Feeding System by Means of Silos with IoT Technology",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44645 supersedes original DOI 10.1016/j.heliyon.2022.e10071; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2022-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.heliyon.2022.e10071",
              "state": "active"
            },
            {
              "at": "2026-02-26T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.heliyon.2026.e44645 supersedes original DOI 10.1016/j.heliyon.2022.e10071; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.heliyon.2026.e44645",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-02-26T00:00:00+00:00",
          "claim_id": "R016",
          "doi": "10.1016/j.heliyon.2022.e10071",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.heliyon.2026.e44645",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.3389/fnut.2024.1520555 supersedes original DOI 10.3389/fnut.2022.803913; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;",
          "chain": [
            {
              "at": "2022-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.3389/fnut.2022.803913",
              "state": "active"
            },
            {
              "at": "2024-11-05T00:00:00+00:00",
              "basis": "Retraction Watch record 10.3389/fnut.2024.1520555 supersedes original DOI 10.3389/fnut.2022.803913; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.3389/fnut.2024.1520555",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-11-05T00:00:00+00:00",
          "claim_id": "R017",
          "doi": "10.3389/fnut.2022.803913",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.3389/fnut.2024.1520555",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1016/j.jogc.2023.102264 supersedes original DOI 10.1016/j.jogc.2023.102264; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;",
          "chain": [
            {
              "at": "2023-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1016/j.jogc.2023.102264",
              "state": "active"
            },
            {
              "at": "2024-09-26T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1016/j.jogc.2023.102264 supersedes original DOI 10.1016/j.jogc.2023.102264; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1016/j.jogc.2023.102264",
              "state": "retracted"
            }
          ],
          "changed_at": "2024-09-26T00:00:00+00:00",
          "claim_id": "R019",
          "doi": "10.1016/j.jogc.2023.102264",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1016/j.jogc.2023.102264",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "The Effect of Preoperative Intravenous Tranexamic Acid Versus Rectal Misoprostol in Reducing Blood Loss During and After Elective Cesarean Delivery in Primigravida: A Double-Blinded, Randomized, Comparative-Placebo Trial",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1007/s00500-026-11208-y supersedes original DOI 10.1007/s00500-021-06668-3; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2022-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1007/s00500-021-06668-3",
              "state": "active"
            },
            {
              "at": "2026-01-21T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1007/s00500-026-11208-y supersedes original DOI 10.1007/s00500-021-06668-3; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1007/s00500-026-11208-y",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-01-21T00:00:00+00:00",
          "claim_id": "R020",
          "doi": "10.1007/s00500-021-06668-3",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1007/s00500-026-11208-y",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Fat-based studies for computer-assisted screening of child obesity using thermal imaging based on deep learning techniques: a comparison with quantum machine learning approach",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2025.2501451 supersedes original DOI 10.1080/14767058.2020.1814239; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2020-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1080/14767058.2020.1814239",
              "state": "active"
            },
            {
              "at": "2025-05-08T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2025.2501451 supersedes original DOI 10.1080/14767058.2020.1814239; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2025.2501451",
              "state": "retracted"
            }
          ],
          "changed_at": "2025-05-08T00:00:00+00:00",
          "claim_id": "R022",
          "doi": "10.1080/14767058.2020.1814239",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2025.2501451",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Omega-3 fatty acids plus vitamin for women with gestational diabetes or prediabetes: a meta-analysis of randomized controlled studies",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2026.2607752 supersedes original DOI 10.1080/14767058.2019.1678132; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
          "chain": [
            {
              "at": "2020-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1080/14767058.2019.1678132",
              "state": "active"
            },
            {
              "at": "2026-01-07T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2026.2607752 supersedes original DOI 10.1080/14767058.2019.1678132; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2026.2607752",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-01-07T00:00:00+00:00",
          "claim_id": "R023",
          "doi": "10.1080/14767058.2019.1678132",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2026.2607752",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Ultrasound markers for prediction of gestational diabetes mellitus in early pregnancy in Egyptian women: observational study",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2026.2654284 supersedes original DOI 10.1080/14767058.2018.1491030; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2018-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.1080/14767058.2018.1491030",
              "state": "active"
            },
            {
              "at": "2026-04-07T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2026.2654284 supersedes original DOI 10.1080/14767058.2018.1491030; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2026.2654284",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-04-07T00:00:00+00:00",
          "claim_id": "R024",
          "doi": "10.1080/14767058.2018.1491030",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2026.2654284",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Maternal, fetal, and neonatal outcomes among different types of hypertensive disorders associating pregnancy needing intensive care management",
          "to_state": "retracted"
        },
        {
          "basis": "Retraction Watch record 10.1080/14767058.2026.2654275 supersedes original DOI 10.3109/14767058.2016.1154526; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
          "chain": [
            {
              "at": "2016-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.3109/14767058.2016.1154526",
              "state": "active"
            },
            {
              "at": "2026-04-09T00:00:00+00:00",
              "basis": "Retraction Watch record 10.1080/14767058.2026.2654275 supersedes original DOI 10.3109/14767058.2016.1154526; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.1080/14767058.2026.2654275",
              "state": "retracted"
            }
          ],
          "changed_at": "2026-04-09T00:00:00+00:00",
          "claim_id": "R025",
          "doi": "10.3109/14767058.2016.1154526",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.1080/14767058.2026.2654275",
          "from_state": "active",
          "memory_status": "retracted_forgotten",
          "title": "Role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial",
          "to_state": "retracted"
        }
      ]
    },
    "dataset": "groundtruth_memory",
    "from": "2023-01-01T00:00:00+00:00",
    "to": "2026-07-04T00:00:00+00:00"
  },
  "to": "2026-07-04T00:00:00+00:00"
}
```

## Verification So Far

- `.\.venv\Scripts\python.exe -m groundtruth.timeline --results-v3-p4` completed and regenerated `data/timeline_run.json` plus this document.
- `.\.venv\Scripts\pytest.exe -q tests\test_timeline.py tests\test_web.py` -> 22 passed, 1 warning in 0.35s.
- `ruff check groundtruth tests web` -> all checks passed.
- `.\.venv\Scripts\python.exe -m compileall -q groundtruth tests web` -> passed.
- `git diff --check` -> passed with only existing CRLF normalization warnings for tracked web/test files.
- `.\.venv\Scripts\pytest.exe -q --durations=10` -> 56 passed, 13 warnings in 124.13s (0:02:04).
- TestClient smoke for `/timeline?from=2023-01-01&to=2026-07-04&question=...Avacopan...` -> 200; changes `added=14`, `contested=0`, `revised=16`, `purged=24`; answer then cites 5 active original claims, answer now cites 5 retraction notices.
