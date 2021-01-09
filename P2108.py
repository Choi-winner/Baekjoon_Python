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

# 입력받기.
n = int(sys.stdin.readline())
numbers = []

sum = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    numbers.append(temp)
    sum += temp


# 산술평균 출력하기.
print('%.0i' % round(sum/n, 0))

# 중앙값 출력하기.
numbers.sort()
print(numbers[int((n-1)/2)])

# 최빈값 출력하기.
freq_numbers = [0]*n

duplication = True # 중복이면 True. 중복이 끝나면 False.
number_n_count = {}
i = 0
while i < n:
    # numbers가 오름차순이니깐,
    # 처음부터 올라가면서 중복인 것들의 갯수를 세고, 그 중에 가장 많은 갯수를 가지는 것을 찾는다.
    # 1 1 1 2 5 6 6 6 6 7

    # 왼쪽의 두 수가 같으면 duple을 1 증가시킨다.
    duple = 1
    while duplication == True:
        if numbers[i] == numbers[i+1]: 
            i += 1 # 다음 numbers의 요소와 또 비교. i는 for문 전체에서 증가.
            duple += 1 # 중복의 갯수가 증가.
            duplication == True
        else:
            duplication = False # while문 탈출.
            number_n_count[numbers[i]] = duple # { 숫자 : 중복된 갯수 } 저장.
            i += 1
    # while loop 끝나고 i가 증가해있어야 하는데...
    print('i: ', i)
# for문이 끝나면 number_n_count 라는 dict에 { 숫자 : 중복된 갯수 } 형태로 저장되어 있음.
print(number_n_count)

max_duple = max(number_n_count.values()) # max_duple에 중복된 횟수의 최댓값이 저장.
print(max_duple)

i = 0
most_freq = 0
for number, count in number_n_count.items():
    if count == max_duple: # 최빈값 1개를 찾았을 때, i = 1
        i += 1
        most_freq = number
    if i == 2: # 최빈값 2개를 찾았을 때, print하고 break
        print(number)
        break
if i == 1:
    print(most_freq)


# dict에 저장된 순서대로 items하는 건가?
# 만약에 무작위로 뽑아보는 거면 이렇게 하면 안된다..


     
''' 최빈값 구하는 부분.
freq_numbers[i] = numbers.count(numbers[i]) # 여기가 제일 오래걸리는 loop
how_many = max(freq_numbers) # 최빈값의 빈도수. 2
if freq_numbers.count(how_many) == 1: # 최빈값이 1개일때.
    index = freq_numbers.index(how_many)
    print(numbers[index])
else: # 최빈값이 여러개일 경우 최빈값 중 2번째로 작은 값을 출력.
    most_freq = [] # 최빈값들을 입력할 리스트.
    for i in range(n):
        if how_many == freq_numbers[i]:
            most_freq.append(numbers[i]) 
            # 중앙값 구할때, numbers를 정렬해뒀기 때문에 most_freq에 들어가는 순서도 작은 것부터 오름차순.
            if len(most_freq) == 2*how_many:
                break
        if len(most_freq) == 2*how_many:
            break

    print(most_freq[how_many]) # 두번째로 큰 최빈값을 출력.
'''



# 범위 출력.
print(numbers[n-1] - numbers[0])