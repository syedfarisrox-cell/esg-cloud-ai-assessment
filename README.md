# Cloud-Enabled ESG Automation – BUS5001 Assessment 3

Experiment logs, code and evidence for **Assessment 3: Robotic Process Automation, AI and Cloud-Enabled ESG Analytics**.

| Question | Folder | Contents |
|---|---|---|
| Q1 ESG chatbot | [`q1-chatbot/`](q1-chatbot/) | Dialogflow CX agent design notes and screenshots |
| Q3 LLM message triage | [`q3-llm-triage/`](q3-llm-triage/) | Prompts (original and revised), labelled test set, rule-based baseline, scoring script, LLM outputs, results |
| Q4 NotebookLM evaluation | [`q4-notebooklm/`](q4-notebooklm/) | Test protocol, experiment log, screenshots |
| Supporting | [`docs/`](docs/) | Demonstration video script |

## Repository structure

```
.
├── q1-chatbot/
│   ├── README.md                 Agent design: intents, entities, pages, routes
│   └── screenshots/              Console and test-agent evidence
├── q3-llm-triage/
│   ├── prompts/                  v1 original and v2 revised prompts, batch and single-run files
│   ├── data/test_messages.csv    12 messages with gold labels
│   ├── baseline/                 rule_based_baseline.py, score.py
│   ├── outputs/                  Baseline predictions and raw LLM JSON outputs
│   └── results/                  scores.json and results summary
├── q4-notebooklm/
│   ├── NotebookLM_test_protocol.md
│   ├── logs/experiment_log.md
│   └── screenshots/
└── docs/video_script.md
```

## Reproducing the Q3 results

Requires Python 3.9 or later. Only the standard library is used.

```bash
cd q3-llm-triage/baseline
python rule_based_baseline.py ../data/test_messages.csv ../outputs/baseline_predictions.json
python score.py ../data/test_messages.csv \
    baseline=../outputs/baseline_predictions.json \
    llm_v1=../outputs/llm_v1_outputs.json \
    llm_v2=../outputs/llm_v2_outputs.json
```

## Responsible use

- All test messages are synthetic. The name and phone number in message M09 are fictitious and were included only to test personal-data handling.
- No real personal or organisational data was uploaded to any AI service.
- AI assistance (Claude) was used for planning, design and drafting, as declared in the assessment's AI acknowledgement. All experiments were run, checked and interpreted by the author.
