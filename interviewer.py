from agents.question_agent import generate_question
from agents.evaluator import evaluate_answer


class Interviewer:

    def __init__(self, job_description, seniority):

        self.job_description = job_description
        self.seniority = seniority

        self.history = []

    def next_question(self):

        history_text = "\n".join(
            str(item) for item in self.history
        )

        question = generate_question(
            self.job_description,
            self.seniority,
            history_text
        )

        return question

    def evaluate(self, question, answer):

        evaluation = evaluate_answer(
            question,
            answer,
            self.job_description
        )

        self.history.append({
            "question": question,
            "answer": answer,
            "evaluation": evaluation
        })

        return evaluation