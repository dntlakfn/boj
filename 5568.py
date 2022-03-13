from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
card_list = [input().rstrip() for _ in range(n)]
card_list = list(permutations(card_list, k))
for i in range(len(card_list)):
    card_list[i] = "".join(card_list[i])
card_list = set(card_list)
print(len(card_list))