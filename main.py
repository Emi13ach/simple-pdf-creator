import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="p", unit="mm", format="A4")

for index, row in df.iterrows():
    for num in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, align="L", txt=row["Topic"])
        pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")
