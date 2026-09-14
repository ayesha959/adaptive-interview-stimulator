from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report, filename="interview_report.pdf"):

    document = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    for line in report.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line.replace("&", "&amp;"),
                    styles["Normal"]
                )
            )

    document.build(story)

    return filename