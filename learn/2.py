# n = int(input())
sale_1 = list(map(int,input().split()))
sale_2 = list(map(int,input().split()))
sale_3 = list(map(int,input().split()))
sale_4 = list(map(int,input().split()))
sales_total = [0]*len(sale_1)
for i in range(len(sale_1)):
    sales_total[i] = sale_1[i]+sale_2[i]+sale_3[i]+sale_4[i]
commision = []
remarks = []
for i in sales_total:
    if i<50000:
        commision.append(0)
    else:
        commision.append((i*(5/100)))
    if i>=80000:
        remarks.append('Excellent')
    elif i>=60000 and i<80000:
        remarks.append('Good')
    elif i>=40000 and i<60000:
        remarks.append('Average')
    elif i<40000:
        remarks.append('Work Hard')
print('Sales Monthly',sales_total)
print('Commsion',commision)
print('Remarks',remarks)
