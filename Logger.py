import json
import os
from datetime import datetime

RESULTS_FILE = "results/evaluations.json"


def log_evaluation(evaluation: dict):
    os.makedirs("results", exist_ok=True)

    existing = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            existing = json.load(f)

    evaluation["timestamp"] = datetime.utcnow().isoformat()
    existing.append(evaluation)

    with open(RESULTS_FILE, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"✅ Logged evaluation. Overall score: {evaluation['overall_score']}/10")
