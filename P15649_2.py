'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 
수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

'''
이 문제를 푸는 방법에 대해서 생각해보자.
우선, 4개의 전역변수를 둔다.
2개는 인풋인 N, M이고,
2개는 out_list, is_used이다.
각각은 원하는 크기의 아웃풋을 저장할 공간과 사용된 숫자와 사용되지 않은 숫자를 구분하는 리스트이다.
재귀함수 out_list_finder에서는 다음으로 찾을 인덱스를 인풋으로 넣는다.
다음으로 찾을 인덱스가 M+1이라면, 이미 M개의 리스트를 만든 상태이기 때문에 재귀를 종료한다.

MAIN 부분에서는 재귀함수의 첫 입력으로 0을 넣어준다.

Depth = 0, 1, ..., (M-1) 이 output list의 인덱스가 된다.
'''


import sys
N, M = map(int, sys.stdin.readline().split())

out_list = [-1]*(M+1)
is_used = [False]*N

# 재귀함수, 찾으려는 수의 개수를 모두 찾으면 재귀함수 탈출,
# 아직 덜 찾았다면, 아직 사용하지 않은 수 중에서 하나 찾기.
def out_list_finder(Depth): # Depth = 결과 리스트에서 다음으로 찾을 인덱스.
    # 재귀함수의 탈출조건 if문.
    if Depth == M:
        for i in out_list[0:M]:
            print(i,' ', end='') # 개행 없이 출력.
        print()
        return # return; 을 파이썬에서 어떻게 구현하나?
    
    # 재귀함수의 재귀 부분.
    # 1개의 숫자를 찾는다. 이때, 탐색하지 않은 숫자를 순서대로 찾음!
    for i in range(0, N):
        if is_used[i] is False:
            out_list[Depth] = i + 1
            is_used[i] = True
            out_list_finder(Depth+1)
            is_used[i] = False # K+1의 재귀가 끝난 후에 꼭 이 과정이 필요 for backtracking
            

# MAIN 함수 부분.

out_list_finder(0)      
