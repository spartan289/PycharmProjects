from fpdf import FPDF
f = open('question.txt','r')
flag=0
write = open('text.txt','w')
c=1
for i in f:
    if flag==1:
        if i.startswith("Program"):
            write.close()
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=10)
            read = open('text.txt', 'r')
            for x in read:

                pdf.cell(200, 10, txt=x, ln=1)
            pdf.output("Program{}.pdf".format(c))
            c+=1
            write = open('text.txt','w')
            write.truncate()
            flag=0
    if i.startswith("Program"):
        write.write(i)
        flag=1
        continue
    write.write(i)




