# LLM-as-a-Judge Translation Evaluation Pipeline

A practical evaluation pipeline that uses Claude to score translation quality across fluency, accuracy, and cultural appropriateness.

Built by [Temitope Ajao](https://www.linkedin.com/in/) — AI Engineer | LLMs & NLP Systems

---

## What It Does

- Accepts a source text + translated output
- Sends both to an LLM judge with a structured scoring prompt
- Returns scores for **fluency**, **accuracy**, and **cultural appropriateness**
- Logs results to a JSON file for tracking over time
- Supports **batch evaluation** for processing multiple pairs

---

## Project Structure

```
llm-judge-pipeline/
├── evaluator.py       # Core evaluation logic
├── prompts.py         # Judge prompt template
├── logger.py          # Results logger
├── main.py            # Run single or batch evaluations
├── requirements.txt
├── results/
│   └── evaluations.json
└── .env
```

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/yourusername/llm-judge-translation-pipeline.git
cd llm-judge-translation-pipeline
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create your `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

4. Run:

```bash
python main.py
```

---

## Sample Output

```json
{
  "fluency": {
    "score": 9,
    "reason": "The translation reads naturally and follows Yoruba grammatical structure."
  },
  "accuracy": {
    "score": 8,
    "reason": "Core meaning is preserved; minor phrasing differences don't affect intent."
  },
  "cultural_appropriateness": {
    "score": 9,
    "reason": "Terminology is appropriate for a Nigerian Yoruba-speaking audience."
  },
  "overall_score": 8.67,
  "recommendation": "pass"
}
```

---

## Read the Full Tutorial

[Building an LLM-as-a-Judge Evaluation Pipeline for Translation Quality](#) — dev.to
