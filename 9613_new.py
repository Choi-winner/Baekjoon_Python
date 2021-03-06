# GCD (최대공약수) 의 합
'''
문제
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 
다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

출력
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.

예제 입력 1 
3
4 10 20 30 40
3 7 5 12
3 125 15 25

예제 출력 1 
70
3
35

'''
'''
최대공약수를 구하는 방법은, 
각 수의 소인수분해를 먼저 하고, 이 소인수분해된 결과를 바탕으로 공통인 소인수를 모두 
4 10 30 이라면, 
소인수분해 -> 2^2, 2*5, 2*3*5 로 소인수분해되고,

이 결과를 바탕으로 공통으로 존재하는 소인수를 모두 조사, -> 2
각 소인수가 최대 몇 개씩 있는 지 조사 -> 2:1개
이 조사 결과를 모두 곱하면 최대공약수가 만들어짐. 

'''
import sys

# 유클리드 호제법으로 GCD를 구하면 O(logN)으로 가능!
# a > b 라고 가정하고 시작.
def gcd_u(a, b):
    if b == 0:
        return a
    return gcd_u(b, a % b)

    
T = int(sys.stdin.readline())
for i in range(T):
    l = list(map(int, sys.stdin.readline().split()))
    n = l[0]
    l = l[1:]    
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            a = max(l[i], l[j])
            b = min(l[i], l[j])
            sum += gcd_u(a, b)
    print(sum)    
    
    