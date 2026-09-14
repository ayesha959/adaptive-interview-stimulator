import streamlit as st

from services.interview_engine import InterviewEngine
from agents.report_agent import generate_report
from services.pdf_service import create_pdf


st.set_page_config(
    page_title="Adaptive Interview Simulator",
    page_icon="🎯"
)


st.title("🎯 Adaptive Interview Simulator")

st.write(
    "An interview that actually reacts to what you just said."
)


# --------------------------------
# SETUP
# --------------------------------

if "engine" not in st.session_state:

    st.session_state.engine = None

if "question" not in st.session_state:

    st.session_state.question = None

if "turn" not in st.session_state:

    st.session_state.turn = 0

if "history" not in st.session_state:

    st.session_state.history = []


# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.header("Interview Setup")


job_description = st.sidebar.text_area(
    "Job Description",
    height=250
)


seniority = st.sidebar.selectbox(
    "Seniority",
    [
        "Fresher",
        "Junior",
        "Mid-Level",
        "Senior"
    ]
)


if st.sidebar.button("Start Interview"):

    if not job_description:

        st.error("Please enter a job description.")

    else:

        st.session_state.engine = InterviewEngine(
            job_description,
            seniority
        )

        st.session_state.turn = 1

        st.session_state.history = []

        st.session_state.question = (
            st.session_state.engine.get_question()
        )

        st.rerun()


# --------------------------------
# INTERVIEW
# --------------------------------

if st.session_state.engine:

    st.subheader(
        f"Question {st.session_state.turn}"
    )

    st.info(
        st.session_state.question
    )


    answer = st.text_area(
        "Your Answer",
        height=200
    )


    if st.button("Submit Answer"):

        if not answer:

            st.warning(
                "Please enter your answer."
            )

        else:

            evaluation = (
                st.session_state.engine.submit_answer(
                    st.session_state.question,
                    answer
                )
            )


            st.session_state.history.append({

                "question":
                    st.session_state.question,

                "answer":
                    answer,

                "evaluation":
                    evaluation
            })


            st.subheader("Why this follow-up?")

            st.write(evaluation)


            st.session_state.turn += 1


            if st.session_state.turn <= 8:

                st.session_state.question = (
                    st.session_state.engine.get_question()
                )

                st.rerun()

            else:

                st.success(
                    "Interview completed!"
                )


# --------------------------------
# FINAL REPORT
# --------------------------------

if (
    st.session_state.engine
    and st.session_state.turn > 8
):

    st.header("📊 Final Report")


    if st.button("Generate Final Report"):

        report = generate_report(
            job_description,
            st.session_state.history
        )


        st.markdown(report)


        filename = create_pdf(report)


        with open(filename, "rb") as file:

            st.download_button(
                label="📥 Download PDF",
                data=file,
                file_name="interview_report.pdf",
                mime="application/pdf"
            )