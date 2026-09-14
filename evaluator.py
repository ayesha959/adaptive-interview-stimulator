from services.gemini_service import generate_response


def evaluate_answer(question, answer, job_description):

    prompt = f"""
You are an interview evaluator.

JOB DESCRIPTION:
{job_description}

QUESTION:
{question}

CANDIDATE ANSWER:
{answer}

Evaluate the answer.

Return:

Score: X/10

Strengths:
- ...

Weaknesses:
- ...

Missing concepts:
- ...

Recommendation:
- Probe deeper
OR
- Move to next topic
"""

    return generate_response(prompt)