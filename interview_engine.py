from agents.interviewer import Interviewer


class InterviewEngine:

    def __init__(self, job_description, seniority):

        self.interviewer = Interviewer(
            job_description,
            seniority
        )

    def get_question(self):

        return self.interviewer.next_question()

    def submit_answer(self, question, answer):

        return self.interviewer.evaluate(
            question,
            answer
        )

    def get_history(self):

        return self.interviewer.history