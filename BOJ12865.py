'''
문제
이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 
세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
'''
''' 배낭 문제 해결 방법
1. 순서대로 물건을 하나씩 탐색.
2. 재귀함수에 knapsack( 남은 용량, 현재 탐색 물건의 인덱스 ) = k(cap, n)
    용량이 0이거나 물건이 끝났으면 return 0
    용량에 비해 인덱스의 물건의 사이즈(혹은 무게)가 크면 다음 인덱스의 물건에 대해서 knapsack( cap, n-1 )
    용량에 물건이 들어갈 수 있으면, 해당 물건을 넣고 계속 탐색한 결과와 해당 물건을 안넣고 탐색한 결과 비교해서 큰 값을 return (재귀호출)
'''

import sys
N, K = map(int, sys.stdin.readline().split())
# N = 물품의 수, K = 버틸 수 있는 최대 무게
w_list = []
v_list = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    w_list.append(w)
    v_list.append(v)
    # w_list[i] 의 무게를 가진 물건의 가치는 v_list[i]

def knapsack(cap, n):
    if cap == 0 or n == 0:
        return 0
    elif cap < w_list[n]:
        return knapsack(cap, n-1) # 다음 항목 조사
    else:
        return max( v_list[n] + knapsack(cap - w_list[n], n-1 ), knapsack(cap, n-1)) 

max_value = knapsack(K, N-1)
print(max_value)