import json
from evaluator import evaluate_translation, batch_evaluate
from logger import log_evaluation

# --- Single evaluation example ---
source = "Please ensure the patient takes the medication twice daily with food."
translation = "Jọwọ rii daju pe alaisan mu oogun naa lẹmeji lojoojumọ pẹlu ounjẹ."
target_language = "Yoruba"

result = evaluate_translation(source, translation, target_language)
log_evaluation(result)
print(json.dumps(result, indent=2))


# --- Batch evaluation example ---
pairs = [
    {
        "source": "Welcome to our platform.",
        "translation": "Kaabọ si pẹpẹ wa.",
        "target_language": "Yoruba"
    },
    {
        "source": "Your payment was successful.",
        "translation": "Isanwo rẹ ti ṣaṣeyọri.",
        "target_language": "Yoruba"
    }
]

results = batch_evaluate(pairs)
for result in results:
    log_evaluation(result)
