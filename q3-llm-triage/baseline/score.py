"""
Score one or more prediction files against the labelled test set (Q3b).

Accepts either format:
  {"M01": {"issues": [...]}, ...}                    (baseline output)
  {"results": [{"id": "M01", "issues": [...]}, ...]} (LLM batch output)

Usage:
    python score.py ../data/test_messages.csv baseline=../outputs/baseline_predictions.json \
        llm_v1=../outputs/llm_v1_outputs.json llm_v2=../outputs/llm_v2_outputs.json
"""
import csv
import json
import sys

TEAM_FOR = {
    "water_leak": "Facilities Maintenance",
    "energy_waste": "Energy & Sustainability",
    "waste_recycling": "Waste & Recycling",
    "hazardous_disposal": "Health, Safety & Environment",
    "safety_emergency": "Health, Safety & Environment",
    "accessibility": "Accessibility & Inclusion",
    "procurement_supplier": "Procurement",
    "governance_conduct": "Governance & Compliance",
    "other": "Human Review Queue",
}
RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}


def load_predictions(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "results" in data:
        return {r["id"]: r for r in data["results"]}
    if isinstance(data, list):
        return {r["id"]: r for r in data}
    return data


def norm(value):
    return str(value).strip().upper() if value is not None else ""


def as_bool(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("true", "y", "yes", "1")


def primary_issue(pred, accepted):
    """Score the issue that matches the gold category if the model reported it;
    otherwise score the model's highest-urgency issue."""
    issues = pred.get("issues") or [pred]
    matching = [i for i in issues if str(i.get("issue_category", "")).strip().lower() in accepted]
    pool = matching or issues
    return max(pool, key=lambda i: RANK.get(norm(i.get("urgency")), -1)), issues


def score(rows, preds):
    totals = {"category": 0, "urgency": 0, "team": 0, "escalation": 0, "sensitivity": 0}
    details = []
    for row in rows:
        pred = preds.get(row["id"])
        if pred is None:
            details.append({"id": row["id"], "error": "missing prediction"})
            continue
        accepted = {row["gold_category"]} | ({row["alt_category"]} if row["alt_category"] else set())
        issue, issues = primary_issue(pred, accepted)
        cat = str(issue.get("issue_category", "")).strip().lower()
        team = str(issue.get("recommended_team", "")).strip()
        result = {
            "id": row["id"],
            "category": cat in accepted,
            "urgency": norm(issue.get("urgency")) == row["gold_urgency"],
            "team": team in {TEAM_FOR[c] for c in accepted},
            "escalation": as_bool(issue.get("escalate_to_human")) == as_bool(row["gold_escalate"]),
            "sensitivity": norm(issue.get("data_sensitivity_risk")) == row["gold_sensitivity"],
            "pred_category": cat,
            "pred_urgency": norm(issue.get("urgency")),
            "n_issues": len(issues),
        }
        if row["second_category"]:
            found = {str(i.get("issue_category", "")).lower() for i in issues}
            result["found_second_issue"] = row["second_category"] in found
        for k in totals:
            totals[k] += int(result[k])
        details.append(result)
    n = len(rows)
    return {k: f"{v}/{n} ({v / n:.0%})" for k, v in totals.items()}, details


def main():
    rows = list(csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8")))
    summary = {}
    for arg in sys.argv[2:]:
        name, path = arg.split("=", 1)
        totals, details = score(rows, load_predictions(path))
        summary[name] = {"accuracy": totals, "per_message": details}
        print(f"\n=== {name} ===")
        for k, v in totals.items():
            print(f"  {k:<12} {v}")
        print("  errors:")
        for d in details:
            wrong = [k for k in ("category", "urgency", "team", "escalation", "sensitivity") if not d.get(k)]
            extra = "" if d.get("found_second_issue", True) else " | missed second issue"
            if wrong or extra:
                print(f"    {d['id']}: wrong {wrong} (pred {d.get('pred_category')}/{d.get('pred_urgency')}){extra}")
    with open("../results/scores.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print("\nSaved ../results/scores.json")


if __name__ == "__main__":
    main()
