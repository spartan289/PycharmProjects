# print prime number 1 to 100 in one line
print([i for i in range(2,201) if not [j for j in range(2,i) if i%j ==0]])