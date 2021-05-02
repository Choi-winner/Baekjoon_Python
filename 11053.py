'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 
A = {10, 20, 30, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

6
1 1 3 2 8 0

'''
import sys
N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
ll = [ [] for _ in range(N) ]

for i in range(N):
    a = l[i]
    for j in range(1, N-i):
        if a < l[i+j]:
            ll[i+j].append(i) # ll[i][j] = i 번째 수로 올 수 있는 수들의 인덱스 리스트.

print(ll) 
            
l_len = [ 1 for _ in range(N)] # l_len[i] = l[i]에 올 때까지 가장 긴 증가수열의 길이

for i in range(1, N):
    temp = []
    if len(ll[i]) == 0: # 만약 이 수 이전에 올 수 있는 수가 전혀 없다면, 그냥 continue. (l_len[i] = 1로 그대로 유지) 
        continue
    for j in ll[i]: # 
        temp.append(l_len[j]) # 이전에 올 수 있는 수들이 가진 가장 긴 증가수열의 길이를 모두 temp에 저장
    ans = max(temp) + 1 # 그 수 중 가장 긴 길이에 1을 더하면 답.
    l_len[i] = ans # l_len[i] 에 저장. 

print(max(l_len))

        

