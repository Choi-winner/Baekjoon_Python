'''
문제
어떤 정수 수열에서 0개 이상의 숫자를 지우면 이 수열의 부분 수열 (subsequence) 를 얻을 수 있다. 
예를 들어 10 7 4 9 의 부분 수열에는 7 4 9, 10 4, 10 9 등이 있다. 
단, 10 4 7 은 원래 수열의 순서와 다르므로 10 7 4 9 의 부분 수열이 아니다.

어떤 부분 수열이 순증가할 때 이 부분 수열을 증가 부분 수열 (increasing subsequence) 라고 한다. 
주어진 수열의 증가 부분 수열 중 가장 긴 것의 길이를 계산하는 프로그램을 작성하라.

어떤 수열의 각 수가 이전의 수보다 클 때, 이 수열을 순증가 한다고 한다.

입력
입력의 첫 줄에는 테스트 케이스의 수 C (<= 50) 가 주어진다. 
각 테스트 케이스의 첫 줄에는 수열에 포함된 원소의 수 N (<= 500) 이 주어진다. 
그 다음 줄에 수열이 N개의 정수가 주어진다. 각 정수는 1 이상 100,000 이하의 자연수이다.

출력
각 테스트케이스마다 한 줄씩, 주어진 수열의 가장 긴 증가 부분 수열의 길이를 출력한다.

예제 입력
3
4
1 2 3 4
8
5 4 3 2 1 6 7 8 
8
5 6 7 8 1 2 3 4
예제 출력
4
4
4

'''

import sys
C = int(sys.stdin.readline())
L_list = []
S_list = []
for i in range(C):
    l = int(sys.stdin.readline())
    L_list.append(l)
    s = list(map(int, (sys.stdin.readline()).split()))
    S_list.append(s)

# 입력으로 인덱스(수열의 인덱스) i를 받으면 그 인덱스에 해당하는 수 S[i]보다 크면서, i보다 뒤에 있는 수열에서의 부분 수열을 구한다. 
# 입력으로 인덱스를 받으면, 그 인덱스부터 시작하는 새로운 수열에서 lis의 길이를 반환한다. <- 이게 최적 부분 구조!
# 아래의 함수에서 입력으로 s도 함께 전달하지만, s는 cache에 포함되지 않고, lis()함수 내에서 전역변수의 역할을 할 뿐이다.


for i in range(C):
    s = S_list[i]
    l = L_list[i]
    
    # memoization을 한다. 수열의 길이가 최대 500이므로 501의 크기를 가지는 cache를 사용!
    cache = [-1]*501 # cache[i] = i부터 시작하는 서브 문자열의 lis
    def lis(index):
        # 캐쉬에 이미 값이 있다면, 있는 값을 바로 사용!
        if cache[index] != -1:
            return cache[index]
        ret = 1 # 입력으로 들어온 수 1개가 이미 있기 때문에 반환되는 문자열의 길이는 1이 기본 값이다.
        j = 1
        while index + j < len(s):
            if s[index] < s[index + j]:
                ret = max( ret , lis(index+j) + 1 ) 
            j += 1
        cache[index] = ret
        return ret

    print(i+1, '번째 입력에 대한 LIS의 길이는 ', lis(0))