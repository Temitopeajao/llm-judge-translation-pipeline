JUDGE_PROMPT = """
You are an expert translation evaluator with deep knowledge of linguistics and cultural context.

You will be given:
- SOURCE: The original text
- TRANSLATION: The translated output to evaluate

Evaluate the translation on three dimensions and return ONLY a JSON object:

{{
  "fluency": {{
    "score": <1-10>,
    "reason": "<one sentence explanation>"
  }},
  "accuracy": {{
    "score": <1-10>,
    "reason": "<one sentence explanation>"
  }},
  "cultural_appropriateness": {{
    "score": <1-10>,
    "reason": "<one sentence explanation>"
  }},
  "overall_score": <average of the three scores>,
  "recommendation": "<pass | review | reject>"
}}

SOURCE: {source}
TRANSLATION: {translation}
TARGET LANGUAGE: {target_language}
"""
