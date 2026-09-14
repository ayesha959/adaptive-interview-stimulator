from services.gemini_service import generate_response
from rag.retriever import retrieve_context


def generate_question(job_description, seniority, history):

    context = retrieve_context(job_description)

    prompt = f"""
You are an adaptive technical interviewer.

JOB DESCRIPTION:
{job_description}

SENIORITY:
{seniority}

INTERVIEW HISTORY:
{history}

RELEVANT KNOWLEDGE:
{context}

Your task:

Generate ONE interview question.

Rules:

1. Do not repeat previous questions.
2. Adapt the question based on the candidate's previous answer.
3. Probe weak areas.
4. Move forward when the candidate demonstrates strong knowledge.
5. Increase difficulty gradually.
6. Keep the question realistic for the seniority level.

Return ONLY the interview question.
"""

    return generate_response(prompt)