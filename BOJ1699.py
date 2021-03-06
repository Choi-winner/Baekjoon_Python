'''
문제
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 
예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 
11의 경우 11=22+22+12+12+12(5개 항)도 가능하다.
 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 
 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

출력
주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

예제 입력 1 
7
예제 출력 1 
4
'''
# DP 프로그래밍.
'''
1. 식 정의
d[i] = i를 합으로써 표현할 수 있는 제곱수의 최소 개수.
2. 식 세우기
d[i] = min( d[i], d[i - j*j] + 1 ) for the all j which is (i - j*j) >= 1
3. 식 초기화
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1 # 2^2 
d[5] = 2 # 2^2 + 1^2
d[6] = 3 # 2^2 + 1^2 + 1^2
d[7] = 4 # 4 + 1 + 1 + 1
d[8] = 2 # 4 + 4

초기화는 그냥 d[i] = i 로 모두 1을 i번 더해서 만들었다고 가정하고 초기화. 
그러면 이게 max 값이고, min을 찾으면 될 것.
'''

import sys
import math
n = int(sys.stdin.readline())

d = [ i for i in range(0,n+1) ] # d[0]은 쓰레기. d[1] = 1, ...

for i in range(2, n+1):
    # j의 범위: i > j*j 인 최대 j 까지.

    for j in range(1, int(math.sqrt(i)) + 1 ):
        if i < j*j:
            continue 
        if d[i] > (d[i - j*j] + 1):
            d[i] = (d[i - j*j] + 1)
        # d[i] = min( d[i], d[i - j*j] + 1)
print(d[n])