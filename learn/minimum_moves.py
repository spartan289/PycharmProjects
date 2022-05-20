# Pick any non-negative integer X and update A = A | X

# Add 1 to A, i.e. update A = A + 1
# Add 1 to B, i.e. update B = B + 1
# Here "|" represents the  operator.
# Note: You can choose different X in different moves.
s = 'abc'
def find_numberofmoves(a, b):
    if a>=b:
        return a-b
    elif b==(a|b):
        return 1
    elif b==a+1:
        return 1
    elif b==((a+1)|b):
        return 2
    elif a+2==b:
        return 2
    elif b-1==(a|(b-1)):
        return 2
    elif b+1==(a|(b+1)):
        return 2
    else:
        return 3

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(find_numberofmoves(a,b))
