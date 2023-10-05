from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",  format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")

page_height = 297
page_width = 210
title_height = 12
footer_y = 277

for index, row in df.iterrows():
    pdf.add_page()
    topic = row["Topic"]
    pages = row["Pages"]
    pdf.set_font(family="Times", style="B", size=18)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=title_height, txt=topic, align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    # Footer
    pdf.ln(footer_y - title_height)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, align="R")

    for page in range(pages - 1):
        pdf.add_page()

        # Footer
        pdf.ln(footer_y)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=topic, align="R")

pdf.output("output.pdf")