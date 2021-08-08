from math import ceil
def minStoneSum(piles: list[int], k: int) -> int:
    piles.sort()
    n = len(piles)
    for i in range(k):
        x =n-1
        piles[x] = ceil(piles[x]/2)
        if n-2<0:
            n = len(piles)
        if piles[n-2]>piles[x]:
            n-=1
    return sum(piles)
print(minStoneSum( piles = [7057,6448], k = 4))
