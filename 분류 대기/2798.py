# 2789번 블랙잭

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards_comb = list(combinations(cards, 3))
cards_sum = []
for comb in cards_comb:
    t = sum(comb)
    if t <= m:
        cards_sum.append(t)
print(max(cards_sum))