from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",  format="A4")
pdf.set_font(family="Times", style="B", size=18)
pdf.set_text_color(100, 100, 100)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    topic = row["Topic"]
    pages = row["Pages"]
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)
    for page in range(pages - 1):
        pdf.add_page()

pdf.output("output.pdf")