'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# 입력 방법은 input() 말고 sys.stdin.readline()d 을 쓰는 법을 배워보자.

# Counting sort 알고리즘 배워보자.
''' <Counting sort 알고리즘 정리>
comparison sort 기법은 항상 복잡도가 O(n*log(n)) 이상이다.
이것을 non-comparison 기법을 활용하여 최대한 O(n)까지 낮추는 것이 목표.
예를 들어 인풋이 input array = [2, 0, 1, 4, 5, 4, 3, 2, 0, 1, 1, 0, 5, ,4 3] 이라면,
1. 각 원소들의 성질의 범위를 파악한다. 
    -> 지금은 0과 양의 정수.
2. 각 iteration에서 0, 1, 2, 3, 각각의 원소가 몇 번씩 나왔는지의 빈도 수를 파악한다. 
    그러면 counting array = [3, 3, 2, 2, 3, 2] 이다. 
    "counting array[index] = index의 빈도수"(0부터 시작하는 양의 정수니깐!)
3. counting array에서 빈도수를 쌓아나간다.
    각 요소의 값을 직전의 요소 값에 추가 합산.
    counting array = [3, 6, 8, 10, 13, 15]
4. output array를 input array와 같은 길이로 만들어 준다.
    counting array의 의미는 다음과 같다.
    counting array[0] = 3 : 0은 output array[0]에서 output array[2]까지 3자리 차지한다.
    counting array[1] = 6 : 1은 output array[3]에서 output array[5]까지 3자리 차지한다.
5. input array의 요솟값을 역순으로 output array에 채워넣는다.
    input array의 마지막 요소가 3이라면, counting array[3]을 본다. 10이 들어있다.
    output array의 index = 9 자리에 3이 있어야 한다는 뜻이다.
    output array[9] = 3 을 하고, counting array[3] -= 1 을 해준다.
결과 -> output array = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5]처럼 정렬된 array
'''

import sys
# 한 줄의 입력을 받을때, sys.stdin.readline() 이 1줄을 반환한다.
n = int(sys.stdin.readline()) 

input_array = []
# 여러 줄의 입력을 받을 때, sys.stdin 자체가 하나의 list가 되는 듯
for i in range(n):
    input_array.append(int(sys.stdin.readline().strip()))
# sys.stdin.readline() -> \n까지를 읽어오기.
# strip() -> 뒤에 개행문자를 자동으로 삭제.
# split() -> 공백을 기준으로 나누기.
# split(''\n) -> 마지막에 '' 하나 넣어주기.

LIMIT = 10000
# 1. 입력되는 요소들은 1 ~ 10,000 이다.
counting_array = [0] * (LIMIT + 1)

# 2. counting array 작성.
for i in range(LIMIT): 
    # i = 0 일때 counting array[0] = 1의 개수.
    # i = 1 일때 counting array[1] = 2의 개수. 
    # 즉, counting array[i]
    counting_array[i] = input_array.count(i + 1) # 1의 개수를 인덱스 0 자리에 입력.

# 3. counting array 업데이트. 
for i in range(LIMIT-1):
    counting_array[i+1] += counting_array[i]

# 4. output array 생성.
output_array = [0] * n

# 5. output array 업데이트.
for i in range(n): 
    index = - i + (n - 1) # index는 n-1부터 시작해서 0까지 내려오는 수.
    output_array[counting_array[input_array[index]-1] - 1] = input_array[index]
    counting_array[input_array[index]-1] -= 1

for i in range(n):
    print(output_array[i])

# counting array와 output array 중 하나가 없어도 되지 않을까?
# 혹은 둘 다 없이 print를 바로 해도 되지 않을까?
# 정석적으로 sorted된 list는 위의 코드와 같이 만드는 것이 좋지만 메모리나 속도의 관점에서는 P10989_new 와 같이 하는 것이 좋다.
