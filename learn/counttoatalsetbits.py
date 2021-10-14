import math



def countsetbits(n):
    def powerof2(n):
        if n == 2:
            return 1
        return 2 * powerof2(n // 2) + n // 2
    def countsetbitsform_highpower(n):
        if n <= 0:
            return 0
        return (0 if int(n % 2) == 0 else 1) + countsetbitsform_highpower(int(n / 2))

    def highestpowerof2(n):
        p = int(math.log(n, 2))
        return int(pow(2, p))
    highpowerof2 = highestpowerof2(n)
    sum1 = powerof2(highpowerof2)
    for i in range(highpowerof2,n+1):
        sum1+=countsetbitsform_highpower(i)
    return sum1
print(countsetbits(16))
from math import log2
def countsetbits(n):
    def count_set_bits(n):

        if n == 0 or n == 1:
            return n

        x = int(log2(n))
        bitsupto2raisex = x * (1 << (x - 1))
        msbupto2raisexton = n - (1 << x) + 1
        rest = n - (1 << x)
        ans = bitsupto2raisex + msbupto2raisexton + count_set_bits(rest)
        return ans

