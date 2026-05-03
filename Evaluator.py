import os
import json
import anthropic
from dotenv import load_dotenv
from prompts import JUDGE_PROMPT

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def evaluate_translation(source: str, translation: str, target_language: str) -> dict:
    prompt = JUDGE_PROMPT.format(
        source=source,
        translation=translation,
        target_language=target_language
    )

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_response = message.content[0].text

    try:
        result = json.loads(raw_response)
    except json.JSONDecodeError:
        import re
        json_match = re.search(r'\{.*\}', raw_response, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
        else:
            raise ValueError("Could not parse JSON from model response")

    return result


def batch_evaluate(pairs: list[dict]) -> list[dict]:
    """Evaluate multiple source/translation pairs"""
    results = []
    for pair in pairs:
        result = evaluate_translation(
            source=pair["source"],
            translation=pair["translation"],
            target_language=pair["target_language"]
        )
        result["source"] = pair["source"]
        result["translation"] = pair["translation"]
        results.append(result)
    return results
