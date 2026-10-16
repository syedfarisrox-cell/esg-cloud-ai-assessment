# Q1 – EcoReport: ESG Sustainability Assistant (Dialogflow CX)

**Use case:** sustainability incident reporting. Staff report water leaks, energy waste, recycling contamination, unsafe disposal and accessibility barriers. Each report is risk-triaged and routed to the accountable team.

## Agent components

| Component | Items |
|---|---|
| Intents | `Default Welcome Intent`, `report.incident`, `safety.emergency`, `talk.to.human`, `confirmation.yes`, `confirmation.no` |
| Custom entities | `@incident_type`, `@building`, `@yes_no`, `@contact_choice` |
| System entities | `@sys.any` |
| Pages | Start, Collect Incident Details, Urgent Flag, Confirm Report, Submit Report, Emergency, Human Handoff, End Session |
| Flow-level routes | `safety.emergency`, `talk.to.human` on the Start page |
| Event handlers | `sys.no-match-default` (re-lists options, offers a person), `sys.no-input-default` |

## Key routing conditions

```
$page.params.status = "FINAL" AND $session.params.risk_to_people = "yes"  -> priority HIGH -> Urgent Flag
$page.params.status = "FINAL" AND $session.params.risk_to_people = "no"   -> priority STANDARD -> Confirm Report
```

## Simulator tests

1. Anonymous happy path with slot pre-filling
2. Urgent path (risk = yes, priority HIGH)
3. Emergency raised mid-form
4. Unrecognised input, then fallback, then human handoff

## Folders

- `screenshots/`: flow graph, intents, entities, pages, test transcripts.
