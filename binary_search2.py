'''
N개의 숫자가 나열된 리스트에서 4개의 서로 다른 수를 뽑아서 
4개의 수의 합이 M이면 1 출력, M이 아니면 0 출력
M = 1 ~ 10^8
N = 1 ~ 10^3
l의 원소 각각은 1 ~ 10^8

10 17
1 2 3 4 5 6 7 8 9 10
True(1 2 6 8 )

10 40
1 2 3 4 5 6 7 8 9 10
False

100,000,000
1억번(10^8) 이내의 연산으로 풀자.

아이디어 1: N개의 숫자에서 4개를 뽑는 경우의 수는 N^4 번의 연산이 필요. -> O(N^4)
아이디어 2: N개의 숫자를 먼저 내림차순으로 sort하고( O(N*log(N)) ), 
        가장 왼쪽에 있는 가장 큰 수들부터, 이 수가 너무 크면 안된다. 
        왼쪽에 수가 너무 크면 오른쪽 끝으로 가서 작은 수 들 중에 3개를 뽑아야한다.

        왼족 끝의 가장 큰 수가 a라면, 그 다음에는 남은 리스트에서 3개의 수를 더 뽑아 M - a를 만들어야한다.
        남은 리스트에서 가장 왼쪽의 가장 큰 수가 b라면, M - a - b >= 0라면, b를 선택하고 남은 리스트에서 2개를 더 뽑아 M-a-b를 만든다.
        만약 M-a-b <= 0 이라면 b말고 다음 수를 탐색.
        4개의 수를 뽑았는데, M-a-b-c-d == 0 이면 True 출력.
아이디어 3: 4장 중에 3개까지는 차례대로 뽑고, 나머지 1개를 binary search로 뽑는 방법!

'''

import sys

def search(sorted_list, current_num, how_much):
    # base case: how_much만큼 다 뽑은 상황.
    print('sorted_list: ', sorted_list, ' / current_num: ',current_num, ' / how_much: ',how_much)
    if how_much == 0:
        if current_num == 0: # 이전 recursive에서 탐색한 수를 뺐더니 0이 된 경우.
            return True
        else:
            return False


    for i in range(len(sorted_list)): 
        num = sorted_list[i] # i가 커질수록 더 작은 수를 입력하는 것.
        if current_num - num >= 0:
            current_num -= num
            how_much -= 1
            
            # testing
            print('current number: ', num)
            print(sorted_list[i+1:])
            print(current_num)
            print(how_much)

            if search(sorted_list[i+1:], current_num, how_much) == True: # 왼쪽 부분 리스트를 입력하고, target에서 현재 값 빼고 남은 수, 더 뽑을 개수
                return True
            current_num += num # for next iter
            how_much += 1

    # base case2: 모든 list를 다 돌았는데, how_much만큼 다 뽑지 못했다.
    return False


N, M = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

# l을 내림차순으로 정렬한다.
# l = l.sort(reverse=True) # 내림차순으로 정렬은 되는데, list가 아니라 None을 반환한다.
l = sorted(l) # sort()는 None을 반환하는 반면, sorted는 list를 반환하기 때문에 이거 사용!
l.reverse() # 내림차순으로 조작.

print('start!', l)

print(search(l, M, 4))
