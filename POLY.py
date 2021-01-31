# -*- coding: utf-8 -*-


'''
-*- coding: euc-kr -*-
-*- coding: utf-8 -*-

문제

정사각형들의 변들을 서로 완전하게 붙여 만든 도형들을 폴리오미노(Polyomino)라고 부릅니다. 
n개의 정사각형으로 구성된 폴리오미노들을 만들려고하는데, 이 중 세로로 단조(monotone)인 폴리오미노의 수가 몇 개나 되는지 세고 싶습니다. 
세로로 단조라는 말은 어떤 가로줄도 폴리오미노를 두 번 이상 교차하지 않는다는 뜻입니다.



예를 들어 그림 (a)는 정상적인 세로 단조 폴리오미노입니다. 그러나 (b)는 점선이 폴리오미노를 두 번 교차하기 때문에 세로 단조 폴리오미노가 아닙니다. 
(c)는 맨 오른쪽 아래 있는 정사각형이 다른 정사각형과 변을 완전히 맞대고 있지 않기 때문에 폴리오미노가 아닙니다.

n개의 정사각형으로 구성된 세로 단조 폴리오미노의 개수를 세는 프로그램을 작성하세요.

입력

입력의 첫 줄에는 테스트 케이스의 수 C (1≤C≤50)가 주어집니다. 그 후 각 줄에 폴리오미노를 구성할 정사각형의 수 n (1≤n≤100)이 주어집니다.

출력

각 테스트 케이스마다, n개의 정사각형으로 구성된 세로 단조 폴리오미노의 수를 출력합니다. 
폴리오미노의 수가 10,000,000 이상일 경우 10,000,000으로 나눈 나머지를 출력합니다.

예제 입력

3
2
4
92
예제 출력

2
19
4841817
'''
MOD = 10000000
import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

C = int(sys.stdin.readline())
n_list = []
for i in range(C):
    n_list.append(int(sys.stdin.readline()))

# idea: 부분 문제로 나누어 해결한다.
# 부분 문제는 남은 정사각형의 개수가 입력될 때, 그것으로 만들 수 있는 polyomino의 개수를 반환하는 함수.
# 기저 케이스는 남은 정사각형의 개수가 1개일 때, 1을 반환하는 것.
# 남은 정사각형의 개수가 2개이면, 2를 반환.

for i in range(C):
    # cache는 남은 n의 개수가 인덱스이다.
    cache = [ [-1] * 101 for _ in range(101) ]  # cache[i][j] = i개의 정사각형으로 만드는 폴리오미노이되, 첫 줄에는 j개의 정사각형.
    
    n_input = n_list[i]
    # 이 함수는 입력을 남은 n의 개수와 남은 폴리오미노의 첫 줄의 사각형의 개수 first를 함께 입력받는다.
    # 반환할 내용은 remain_n의 개수를 가지고 만들 수 있는 폴리오미노의 개수이다.
    # 이 개수는  앞서 구한 폴리오미노의
    def poly(n, first): # remain_n의 정사각형을 포함하되 first개의 첫 번째 줄을 가지는 폴리오미노의 개수.
        # base case, when n is equare to first <- the only case can exist
        if n == first:
            return 1
        
        # memoization
        if cache[n][first] != -1:
            return cache[n][first]

        ret = 0
        for second in range(1, n - first + 1):
            ret += (first + second - 1) * poly(n - first, second)       
        # if ret != 0:
        #     print('ret: ', ret)
        if ret >= MOD:
            ret %= MOD
            cache[n][first] = ret
            return ret
        cache[n][first] = ret
        return ret 

    print(i+1, '번째 입력에 대한 출력은 ', poly(n_input, 0) ) # first를 0으로 둬도 괜찮을까?