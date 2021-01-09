'''
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

5
1
3
8
-2
2

'''
import sys 
from collections import Counter

# 입력받기. 
n = int(sys.stdin.readline())
numbers = []

sum = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    numbers.append(temp)
    sum += temp


# 산술평균 출력하기.
def mean(sum):
    print('%.0i' % round(sum/n, 0))


# 중앙값 출력하기.
def median(nums):
    nums.sort()
    print(nums[int((n-1)/2)])

# 최빈값 출력하기.
def mod(nums):
    mode_list = Counter(nums).most_common() # [ [ 요소1, 요소1의 갯수 ], [ 요소2, 요소2의 갯수 ], ... ]
    # print('length of mode_dict: ',len(mode_dict))
    # mode_dict[0][1]에는 가장 많은 요소의 갯수.
    # mode_dict[1][1]에는 두번째로 많은 요소의 갯수.
    if len(mode_list) == 1:
        print(mode_list[0][0])
    elif mode_list[0][1] != mode_list[1][1]: # 첫번째와 두번째 최빈값의 빈도수가 다르면, 유일한 최빈값.
        print(mode_list[0][0])
    else: # 첫번째와 두번째의 빈도수가 같다면, 여러개의 최빈값 중 두번째로 작은 수를 출력.
        # 빈도수가 mode_dict[0][1] 인 것들 중에 두번째로 작은 값 출력
        most_freq = []
        for num_n_freq in mode_list:
            if num_n_freq[1] == mode_list[0][1]:
                most_freq.append(num_n_freq)
            else: # 빈도수가 작아지기 시작한 시점.
                break
        most_freq.sort(key=lambda x:x[0]) # list를 첫 번째 요소 기준으로 오름차순 배열.
        print(most_freq[1][0])

# 범위 출력.
def scope(nums):
    print(nums[n-1] - nums[0])

mean(sum)
median(numbers)
mod(numbers)
scope(numbers)