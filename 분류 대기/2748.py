# 2748번 피보나치 수 2

dic = {}

def fibo(n):
    if n in dic:
        return dic[n]
    
    if n == 0:
        dic[0] = 0
        return 0
    elif n == 1:
        dic[1] = 1
        return 1
    else:
        dic[n] = fibo(n - 1) + fibo(n -2)
        return dic[n]

n = int(input())
print(fibo(n))