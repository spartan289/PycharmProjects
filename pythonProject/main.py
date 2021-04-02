n = int(input())
n=n*2
m = (2 * n) - 2
for i in range(0, n):
    for j in range(0, m):
        print(end=" ")
    m = m - 1

    if(i%2==0):
        for k in range(0, i + 1):
            if (k == 0 or k == i ) :

                print('#', end=' ')
            elif (k==1 or k==i-1):
                print('%', end=' ')

            elif  (k == 2 or k == i - 2):
                print('@', end=' ')


            elif (k == 3 or k == i - 3):
                print('&', end=' ')
                k+=2

            else: print("* ", end=' ')
    print(" ")