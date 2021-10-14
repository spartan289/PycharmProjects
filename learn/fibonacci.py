def fibonacci(n):
    assert n>=0 and int(n)==n,"Fibbonaci number cannot be negative number or non integer."

    if n==0 or n==1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)


print(fibonacci(8))
print(factorial(5))
