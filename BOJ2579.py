'''
문제
계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
 <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는
 10 + 20 + 25 + 20 = 75점이 된다.

계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다.
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

예제 입력 1 
6
10
20
15
25
10
20
예제 출력 1 
75

'''

'''
1. DP 식 정의
d[i] = i 번째 계단까지 도달하는 오는 것의 최댓값. 

d[0] = none
ans = d[n]

2. 식 세우기
i = 4 ~ n
d[i] = max( d[i-3] + c[i-1] , d[i-2] ) + c[i]

3. 초기화
d[1] = c[1]
d[2] = c[1] + c[2]
d[3] = max( d[1], d[2] ) + c[3]

-> d[4] = max( d[1] + c[3], d[2] ) + c[4]

'''

# import sys
# n = int(sys.stdin.readline())
# c = [0] # c[0] = 0
# for i in range(n):
#     c.append(int(sys.stdin.readline()))
#     # c[i] = i번째 입력.

# print(c)
# print('len of c',len(c))

# # initializing
# d = [0 for _ in range(302)]
# d[1] = c[1]
# d[2] = d[1] + c[2]
# d[3] = max( c[1], c[2] ) + c[3]
# print('len of d',len(d))

# for i in range(4, n+1): # i = 4 ~ n
#     if i == n + 1:
#         print('runtime error, i=', i)
#     d[i] = max( d[i-3] + c[i-1] , d[i-2] ) + c[i]
#     print('d[{}] = max( d[{}] + c[{}] , d[{}] ) + c[{}] = {}'.format(i, i-3, i-1, i-2, i, d[i]))

# ans = d[n]
# print(ans)

# for i in range(n+2):
#     print('d[{}]: {}'.format(i, d[i]))
    

import sys
n = int(sys.stdin.readline())
c = []
for i in range(n):
    c.append(int(sys.stdin.readline())) # c[i] = i+1번째 입력, c[2] = 3번째 계단의 수
    

print(c)
print('len of c',len(c))

# initializing
d = [0 for _ in range(n+2)]
d[0] = c[0]
d[1] = c[0] + c[1]
d[2] = max( c[0], c[1] ) + c[2]
print('len of d',len(d))

for i in range(3, n): # i = 3 ~ n-1
    d[i] = max( d[i-3] + c[i-1] , d[i-2] ) + c[i]

ans = d[n-1]
print(ans)

for i in range(n+2):
    print('d[{}]: {}'.format(i, d[i]))



