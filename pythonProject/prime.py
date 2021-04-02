def prime(n):
    mul=1
    c=0
    for num in range(1,n):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                mul = mul * num
                c+=1
                if mul > n:
                    break

    return c-1
print(prime(5000))
