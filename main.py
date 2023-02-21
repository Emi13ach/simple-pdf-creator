import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    for num in range(row["Pages"]):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, align="R", txt=row["Topic"])
        # Set the footer
        if num == 0:
            pdf.ln(-270)
            pdf.set_font(family="Times", size=24, style="B")
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, align="L", txt=row["Topic"])
            pdf.line(10, 21, 200, 21)


pdf.output("output.pdf")
