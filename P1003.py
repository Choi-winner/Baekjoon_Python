'''
fibonacci 
0 1 1 2 3 5 8 13 21 ...

0 -> 0
1 -> 1
2 -> 1 0
3 -> 2 1 -> 1 0 / 1
4 -> 3 2 -> 2 1 1 0 -> 1 0 1 / 1 0
5 -> 4 3 -> 3 2 2 1 -> 2 1 1 0 1 0 1 -> 1 0 1 1 0 / 1 0 1
입력이 주어졌을 때,
재귀함수로 피보나치 수열을 구하는 과정에서
fibo(0)과 fibo(1)이 몇 번 호출되는 지를 구하는 알고리즘.
'''

import sys
N = int(sys.stdin.readline())
test_cases = []
for i in range(N):
    test_cases.append(int(sys.stdin.readline()))

def printer(list_len_2):
    print(list_len_2[0],list_len_2[1])


cases = [ [1, 0], [0, 1] ] # 각 요소는 [0의 호출 개수, 1의 호출 개수]
# 미리 cases에 모든 경우를 저장해둔다.
for i in range(2,41):
    cases.append([cases[i-2][0]+cases[i-1][0] , cases[i-2][1]+cases[i-1][1]])

for i in range(N):
    M = test_cases[i]
    printer(cases[M])
