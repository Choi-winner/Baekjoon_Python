'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
import sys
N = int(sys.stdin.readline())

stack = []

def input_sth():
    input_str = sys.stdin.readline()
    input_list = input_str.split()
   # print('input_str: ',input_list)    
    return input_list
    
    
'''
1
push 1

'''

def push(input_int): # stack에 입력된 정수를 push
    stack.append(input_int) # 맨 뒤에 입력.

def pop(): # stack의 가장 위에 있는 정수를 pop(삭제)하여 출력. 아무 정수도 없으면 -1을 출력
    top_index = len(stack)
    remove_int = 0
    if top_index == 0:
        print('-1')
    else:
        remove_int = stack[top_index - 1]
        print(remove_int)
    if len(stack) == 0:
        pass
    else:
        stack.remove(remove_int)

def size(): # stack에 들어있는 정수의 개수를 출력.
    print(len(stack))

def empty(): # stack이 비어있으면 1, 아니면 0을 출력.
    stack_size = len(stack)
    if stack_size > 0:
        print(0)
    else:
        print(1)

def top(): # stack의 가장 위에 있는 정수 하나를 출력. 정수가 없으면 -1을 출력.
    top_index = len(stack)
    if top_index == 0:
        print('-1')
    else:
        print(stack[top_index - 1])



input_list = []

for i in range(N):
    input_list = input_sth()
    order = input_list[0]
    if order == 'push':
        push(input_list[1])
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()
    # print('stack: ', stack)





