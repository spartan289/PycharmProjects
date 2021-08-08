from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size=8)
f = open("question.txt","r")
for x in f:
    pdf.cell(200,10,txt=x,ln=1)
c="Practicle"
pdf.output("{}.pdf".format(c))
