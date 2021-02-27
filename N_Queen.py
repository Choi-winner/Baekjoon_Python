'''
algorithm study.
N-Queens problem.

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

'''

# 함수를 1개 쓸텐데, 이걸 재귀할 예정.
# 탐색여부를 확인하는 리스트가 필요할까?
# 일단 재귀함수 만들고, 탈출조건은 stack의 length가 원하는 개수가 된 것! 
# length of stack == N 이면 해당 stack을 출력
# 
# 유망성 판단은? <- stack에 push하기 전에 이 유망성 판단을 먼저 해야함!
# 조건에 알맞는 지의 여부.
# 조건: 앞서서 선택한 Queen들과 이동할 수 있는 경로가 겹치지 않아야한다.
   

'''
파이썬에서 스택 사용하는 방법.
# init 
stack = [] 

# push
stack.append(element to push)

# pop
top = stack.pop()

# top
top = stack[-1]
'''

import sys
N = int(sys.stdin.readline())

stack = [] # global로 stack 선언. 원소는 [i, j]로 들어갈 예정. 
cnt = 0 # 경우의 수를 세는 변수.

# global인 stack을 사용하고, 
# 앞으로 들어갈 수 있는 자식 노드가 입력되면 그 노드의 유망성 여부를 판단하여 bool 리턴.
def isValid(candid_child): 
    a = candid_child[0] 
    b = candid_child[1] 
    print('a, b: ', a, b)
    if len(stack) == 0: # 최초의 입력은 항상 유망.
        return True
    
    for [i, j] in stack:
        print('i: ', i)
        print('j: ', j)
        if a == i or b == j:
            return False
        for d_a in range(-N, N):
            if a + d_a == i and (b + d_a == j or b - d_a == j):
                print('a_temp, b_temp: ', a + d_a, b + d_a, 'or', b - d_a , ' / (i, j) : ', i, j)
                return False
    return True # 앞을 다 통과했으면 True                

'''
# isValid test
stack.append([1,2])
stack.append([3,3]) # 이러면 [2, 0]만 True를 받을 수 있다.
print('len of stack: ', len(stack))
print('stack: ', stack)

print('[3, 1] is valid? : ', isValid([3, 1]))
print('[0, 0] is valid? : ', isValid([0, 0]))
print('[2, 0] is valid? : ', isValid([2, 0]))
'''

def backtrack_DFS():
    global cnt # 외부의 변수를 참조하여 값을 바꾸고 싶으면 내부에서 global로 선언해주어야 한다.
    if len(stack) == N: # 재귀의 base case. 탈출조건.
        print('성공!!!!!!!!!!!!!!!!! stack: ', stack)
        cnt += 1 # count 증가. <- 여기서 stack pop 안해도 되는건가?
    else:
        if len(stack) == 0:
            i = -1
            j = -1
        else:
            top = stack[-1] # 현재 노드를 파악.
            [i , j] = top
        for n in range(0, N): 
            candid_child = [i+1, n] # 현재 노드의 모든 자식 노드들을 파악.
            if isValid(candid_child) is True: # 유효한 자식 노드라면
                print('valid! candid_child: ', candid_child, ' / 현재 노드: ', i ,j)
                stack.append(candid_child) # stack에 입력하고
                backtrack_DFS() # 재귀 함수 돌린다. 이때에는 아까 stack에 push했던 candid_child가 새로운 현재 노드가 된다.
                stack.pop() # DFS를 위해 현재 노드를 pop.

print('------------시작------------')
backtrack_DFS()
print('cnt: ', cnt)
    

        
        


