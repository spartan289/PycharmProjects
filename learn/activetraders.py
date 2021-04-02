

n = int(input().strip())
customers = []
for _ in range(n):
    customers_item = input()
    customers.append(customers_item)
customers.sort()
corp={}
for c in range(len(customers)):
    if (customers.count(customers[c]) / n * 100)>=5:
        corp[customers[c]] = (customers.count(customers[c])/n*100)
for key in corp:
    print(key)
