#2609번 최대공약수와 최소공배수
import math

a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = a * b // gcd

print(gcd)
print(lcm)
