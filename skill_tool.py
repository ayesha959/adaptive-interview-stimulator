def extract_skills(job_description):

    skills = []

    common_skills = [
        "Python",
        "SQL",
        "RAG",
        "Machine Learning",
        "LangChain",
        "LangGraph",
        "MCP",
        "API",
        "JavaScript",
        "React"
    ]

    text = job_description.lower()

    for skill in common_skills:

        if skill.lower() in text:

            skills.append(skill)

    return skills