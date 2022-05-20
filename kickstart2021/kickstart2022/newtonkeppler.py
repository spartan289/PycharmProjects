
# 8 5
# 3
# 3
# 4
# 2
# 3
# Newton recently discovered his fourth law of motion, and the cunning Keppler has stolen his research and is planning to publish it before Newton. But Newton has encrypted his research with a unique key, and Keppler doesn't know the key, but he knows that the key is the answer to the following problem. Can you help Keppler get his hands on the key? The problem is as follows:
#
# You are given the weights of M different planets and have to place them in N orbits around the Sun. The ith orbit is at a distance of i light years from the Sun. However, in any single orbit, you can place at most one planet; otherwise, the solar system will collapse. The weight of the ith planet is wi.
#
# Assume you have placed the ith planet on the orbit at distance di from the Sun, where 1 ≤ i ≤ M and di≠dj for i≠j. The stability of the Solar System is given by the summation of abs(di-dj)wiwj over all pairs (i, j) such that 1 ≤ i < j ≤ M. Here, abs(x) denotes the absolute value of the integer x. Your goal is to place the planets in such a way that the stability of the Solar System is maximized.
#
# Formally, you have to choose M different positions for the M weights in an array of size N. Assume you have placed the ith weight in dith position, where di≠dj for i≠j. Then, the stability of the array is defined as the summation of abs(di-dj)wiwj over all pairs (i, j) such that 1 ≤ i < j ≤ M. You have to find the maximum stability over all possible arrangements.

n = int(input())
m = int(input())
mass = []
for i in range(m):
    mass.append(int(input()))