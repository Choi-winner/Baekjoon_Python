# finding GCD of multiple numbers b using prime numbers

import sys
from math import sqrt

def eratos(n):
    candid_list = [True for _ in range(n+1)]
    prime_list = []
    
    candid_list[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if candid_list[i]:
            for j in range(i**2, n+1, i):
                candid_list[j] = False
    for i in range(1, len(candid_list)):
        if candid_list[i]:
            prime_list.append(i)
    return prime_list

primes = eratos(5000)

# print(primes)

# 2부터 시작해서 while 다같이 하나의 소수로 나누어 떨어지지 않을 때까지 반복
T = int(sys.stdin.readline())
for _ in range(T):
    l = list(map(int, sys.stdin.readline().split()))
    gcd = 1
    for p in primes:
        iter = True
        while iter:  
            for i in range(len(l)):  
                if l[i] % p != 0: # list의 모든 수가 p로 나누어 떨어지지 않으면 gcd에 p가 곱해지는 일은 없다.
                    iter = False # p에게 더이상 미래는 없다. 이제 p말고 다른 소수를 대상으로 찾자.
                    break
                else: # 나누어떨어진다면, 실제로 나눈 값을 list에 다시 저장한다. <- 이 과정에서 아마 list에 있는 값이 이상해질 것. 하지만 계산에는 상관없다.
                    l[i] = l[i] / p
            if iter: # for문을 iter = True인 상태로 마친 것은 p가 업데이트 되어야한다는 것.
                gcd *= p # for loop를 break없이 끝냈다는 것은 모든 list의 수가 p로 나누어 떨어진 것이므로 p를 gcd에 곱한다.
    print('gcd: ', gcd)


