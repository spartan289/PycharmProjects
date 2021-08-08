from fpdf import FPDF

f = open('question.txt','r')
flag=0
write = open('text.txt','w')
c=1
for i in f:

    if i.startswith("Program"):
        write.write(i)
        flag=1
        continue
    write.write(i)




