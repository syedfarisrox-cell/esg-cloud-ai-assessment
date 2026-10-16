# Q3 – LLM-based ESG message triage

## Experiment design
- **Test set:** `data/test_messages.csv` has 12 synthetic messages with gold labels, set before any model was run. It contains the five messages from the brief plus seven edge cases: a hidden electrical hazard, hazardous waste, positive feedback, personal data with whistleblowing, two issues in one message, a prompt injection, and a vague message.
- **Systems compared:**
  1. Rule-based keyword baseline (`baseline/rule_based_baseline.py`)
  2. LLM with the original prompt from the brief (`prompts/prompt_v1_original.txt`)
  3. LLM with the revised prompt (`prompts/prompt_v2_revised.txt`)
- **LLM runs:** each batch was run in a fresh chat session. The model name and date are recorded in `results/run_log.md`.
- **Scoring:** `baseline/score.py` scores category, urgency, team, escalation and sensitivity against the gold labels. For multi-issue messages, the issue matching the gold category is scored (or the highest-urgency issue if none matches), and detection of the second issue is reported separately.

## Fairness note
The first version of the baseline reused phrases from the test messages and scored 92%. That reflected overfitting, not skill, so it was discarded. The final keyword lists come from the category definitions only.

## Files
| Path | Description |
|---|---|
| `prompts/batch_v1_original_12_messages.txt` | Original prompt applied to all 12 messages (ready to paste) |
| `prompts/batch_v2_revised_12_messages.txt` | Revised prompt applied to all 12 messages (ready to paste) |
| `prompts/single_v2_M01/M09/M11.txt` | Showcase single-message runs |
| `outputs/baseline_predictions.json` | Baseline output |
| `outputs/llm_v1_outputs.json`, `outputs/llm_v2_outputs.json` | Raw LLM JSON outputs |
| `results/scores.json` | Per-message scoring |
| `results/results_summary.md` | Summary table and discussion |
