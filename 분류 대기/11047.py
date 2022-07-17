# 11047번 동전 0

n, k = map(int, input().split())
count = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

coins = sorted(coins, reverse=True)

for coin in coins:
    count += k // coin
    k %= coin

print(count)