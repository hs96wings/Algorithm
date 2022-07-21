#2851번 슈퍼 마리오

mush = []

for _ in range(10):
    mush.append(int(input()))

sum = 0
op = 0

for i in range(10):
    sum += mush[i]
    if sum >= 100:
        op = i
        break

# 100을 넘거나 같은 값과 100과의 오차
front = abs(sum - 100)
#
# 100을 넘기기 전의 값과 100과의 오차
back = abs(sum - mush[op] - 100)

# back이 100에 더 가깝다면
if front > back:
    print(sum - mush[op])
else:
    print(sum)