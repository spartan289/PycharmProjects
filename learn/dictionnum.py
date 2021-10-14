def dictionary_q(n):
    hash = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
    for i in n:
        print(hash[int(i)],end=" ")
    print()

print("Enter the integer",end=" ")
n = input()
dictionary_q(n)
def countfreq(n):
    hash={}
    for i in n:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    print(hash)
print("Enter the string",end=" ")
s = input()
countfreq(s)
