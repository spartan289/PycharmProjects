def main():
    n=int(input("enter number to get prime number "))
    getPrime(n)

def getPrime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1

    if count==2 :
        print("prime")
    else:
        print("not a prime")


if __name__=="__main__":main()