"""
Rule-based baseline classifier for ESG message triage (Q3b).

A simple keyword-matching classifier, written to be transparent and deterministic.
It is the comparison point for the LLM triage prompt.

Usage:
    python rule_based_baseline.py ../data/test_messages.csv ../outputs/baseline_predictions.json
"""
import csv
import json
import re
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

# Keyword lists are drawn from the category definitions only (generic vocabulary).
# Phrases copied from the test messages were deliberately excluded to avoid overfitting.
# Checked in this order: the first category with a keyword hit wins.
CATEGORY_KEYWORDS = [
    ("safety_emergency", ["fire", "smoke", "gas leak", "smell gas", "injured", "injury", "unconscious", "sparks", "emergency"]),
    ("hazardous_disposal", ["battery", "batteries", "chemical", "asbestos", "e-waste", "toxic", "hazardous"]),
    ("water_leak", ["leak", "leaking", "dripping", "burst pipe", "flood", "flooding"]),
    ("energy_waste", ["air conditioning", "aircon", "air-con", "heater", "heating", "lights", "left on", "energy", "electricity"]),
    ("waste_recycling", ["recycling", "recycle", "bins", "rubbish", "contaminated", "landfill", "compost"]),
    ("accessibility", ["accessible", "accessibility", "wheelchair", "ramp", "lift", "elevator", "disability"]),
    ("procurement_supplier", ["supplier", "vendor", "procurement", "purchasing", "contractor"]),
    ("governance_conduct", ["misconduct", "fraud", "bribe", "unethical", "illegal", "harass", "whistleblow", "breach"]),
]

CRITICAL_WORDS = ["fire", "smoke", "gas", "injured", "injury", "unconscious", "sparks", "electrocut", "emergency"]
HIGH_WORDS = ["urgent", "asap", "immediately", "blocked", "flooding", "dangerous", "hazard", "broken", "unsafe"]
MEDIUM_WORDS = ["again", "still", "repeatedly", "every day", "keeps", "ongoing"]

PII_PATTERNS = [
    r"\b0\d{3}\s?\d{3}\s?\d{3}\b",          # Australian mobile number
    r"[\w.+-]+@[\w-]+\.[\w.]+",              # email address
]


def contains_any(text, words):
    return any(w in text for w in words)


def classify(message):
    text = message.lower()

    category = "other"
    for cat, words in CATEGORY_KEYWORDS:
        if contains_any(text, words):
            category = cat
            break

    if contains_any(text, CRITICAL_WORDS):
        urgency = "CRITICAL"
    elif contains_any(text, HIGH_WORDS):
        urgency = "HIGH"
    elif contains_any(text, MEDIUM_WORDS):
        urgency = "MEDIUM"
    else:
        urgency = "LOW"

    sensitivity = "HIGH" if any(re.search(p, text) for p in PII_PATTERNS) else "NONE"
    escalate = urgency == "CRITICAL" or sensitivity == "HIGH" or category == "other"

    return {
        "issues": [{
            "issue_category": category,
            "urgency": urgency,
            "recommended_team": TEAM_FOR[category],
            "escalate_to_human": escalate,
            "data_sensitivity_risk": sensitivity,
        }]
    }


def main(in_path, out_path):
    with open(in_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    predictions = {row["id"]: classify(row["message"]) for row in rows}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(predictions, f, indent=2)
    print(f"Wrote {len(predictions)} predictions to {out_path}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
