from services.gemini_service import generate_response


def generate_report(job_description, history):

    prompt = f"""
You are a senior hiring manager.

JOB DESCRIPTION:
{job_description}

INTERVIEW HISTORY:
{history}

Create a final interview report.

Include:

1. Overall score
2. Technical skills
3. Problem solving
4. Communication
5. Behavioral skills
6. Strengths
7. Weaknesses
8. Recommended areas for improvement
9. Hiring recommendation

Hiring recommendation must be one of:

STRONG HIRE
HIRE
MAYBE
NO HIRE
"""

    return generate_response(prompt)