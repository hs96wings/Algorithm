# 2751번 수 정렬하기 2
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums = sorted(nums)
for num in nums:
    print(num)