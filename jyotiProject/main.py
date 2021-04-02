n=int(input())
if (n == 1918):
        print('26.09.1918')
elif ((n <= 1917) & (n%4 == 0)) or ((n > 1918) & (n%400 == 0 or ((n%4 == 0) & (n%100 != 0)))):
        print('12.09.{}'.format(n))
else:
        print('13.09.%s'.format(n)) 