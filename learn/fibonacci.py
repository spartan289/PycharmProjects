def fibonacci(n):
    assert n>=0 and int(n)==n,"Fibbonaci number cannot be negative number or non integer."

    if n==0:
        return ""
    def header(n):

        if n==0:
            return 0
        if n==1:
            return 1
        return header(n-1)+header(n-2)
    print(header(n-1))
    return fibonacci(n-1)

fibonacci(7)