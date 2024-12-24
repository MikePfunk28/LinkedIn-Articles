from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from markdown import markdown
from io import StringIO
import re

def convert_md_to_pdf(input_file, output_file):
    try:
        # Read and convert Markdown to plain text
        with open(input_file, "r", encoding="utf-8") as file:
            md_content = file.read()
        html_content = markdown(md_content)

        # Clean up HTML tags for the PDF output (basic formatting)
        clean_text = re.sub(r'<[^>]+>', '', html_content)

        # Create PDF
        pdf_canvas = canvas.Canvas(output_file, pagesize=letter)
        pdf_canvas.setFont("Helvetica", 10)
        width, height = letter

        y_position = height - 40  # Start below the top margin
        for line in clean_text.splitlines():
            if y_position < 50:  # Start a new page if nearing the bottom
                pdf_canvas.showPage()
                pdf_canvas.setFont("Helvetica", 10)
                y_position = height - 40
            pdf_canvas.drawString(40, y_position, line.strip())
            y_position -= 12

        pdf_canvas.save()
        print(f"PDF successfully created: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define file paths
input_md_file = r"C:\Users\mikep\LinkedIn-Articles\AWS PartyRock 2024-12-23.md"  # Replace with your Markdown file path
output_pdf_file = r"C:\Users\mikep\LinkedIn-Articles\AI-ML-Foundation_Learning.pdf"  # Desired output path

convert_md_to_pdf(input_md_file, output_pdf_file)
