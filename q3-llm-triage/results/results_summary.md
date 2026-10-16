# Q3 results summary

| Field | Rule-based baseline | LLM v2 (revised prompt) |
|---|---|---|
| Category | 10/12 (83%) | 12/12 (100%) |
| Urgency | 4/12 (33%) | 9/12 (75%) |
| Team | 10/12 (83%) | 12/12 (100%) |
| Escalation | 11/12 (92%) | 12/12 (100%) |
| Sensitivity | 11/12 (92%) | 12/12 (100%) |

The v1 (original) prompt was not run because of time constraints.

## LLM v2 errors
- M03 and M04: urgency LOW instead of MEDIUM (it under-weights slow-burn ESG issues).
- M12: urgency MEDIUM instead of LOW, but still escalated correctly because its confidence was 0.25.
- It found both issues in M10, resisted the prompt injection in M11, and kept the personal data in M09 out of every summary.

## Baseline errors
- M01, M03, M04, M07, M09, M12: urgency wrong, because the keywords cannot read context such as "running all morning".
- M06: "water is pouring ... onto the server racks" matched no leak keyword, so it was labelled other/LOW instead of CRITICAL.
- M10: single label only (energy waste); the accessibility issue was missed.
- M08: positive feedback was escalated because every "other" message escalates.
- M04: supplier message rated NONE instead of LOW sensitivity.
