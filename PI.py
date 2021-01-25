'''
문제
(주의: 이 문제는 TopCoder 의 번역 문제입니다.)

가끔 TV 에 보면 원주율을 몇만 자리까지 줄줄 외우는 신동들이 등장하곤 합니다. 
이들이 이 수를 외우기 위해 사용하는 방법 중 하나로, 숫자를 몇 자리 이상 끊어 외우는 것이 있습니다. 
이들은 숫자를 세 자리에서 다섯 자리까지로 끊어서 외우는데, 
가능하면 55555 나 123 같이 외우기 쉬운 조각들이 많이 등장하는 방법을 택하곤 합니다.

이 때, 각 조각들의 난이도는 다음과 같이 정해집니다:

모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
그 외의 경우 난이도: 10
원주율의 일부가 입력으로 주어질 때, 난이도의 합을 최소화하도록 숫자들을 3자리에서 5자리까지 끊어 읽고 싶습니다. 
최소의 난이도를 계산하는 프로그램을 작성하세요.

입력
입력의 첫 줄에는 테스트 케이스의 수 C (<= 50) 가 주어집니다. 
각 테스트 케이스는 8글자 이상 10000글자 이하의 숫자로 주어집니다.

출력
각 테스트 케이스마다 한 줄에 최소의 난이도를 출력합니다.

예제 입력
5 
12341234 
11111222 
12122222 
22222222 
12673939 
예제 출력
4
2
5
2
14
'''

import sys
C = int(sys.stdin.readline())
numbers = []
for i in range(C):
    temp = list(map(int, list(sys.stdin.readline())))
    numbers.append(temp)

# 모든 숫자가 같은지 판단하는 함수
def delta_is_zero(num_list): # 수열이 리스트로 입력된다.
    n = num_list[0]
    if num_list.count(n) == len(num_list):
        return True
    else:
        return False

# 모든 숫자가 1씩 증가하거나 감소하는(변화하는) 사실을 판단하는 함수.
def delta_is_one(num_list):
    ret = True
    # num_list는 최소 3의 길이를 가진다.
    i = 1
    if num_list[0] + 1 == num_list[1]: # increasing case
        while i < len(num_list):
            if ( num_list[i] + 1 == num_list[i+1] ):
                continue
            else:
                ret = False
            i += 1
    elif num_list[0] - 1 == num_list[1]: # decreasing case
        while i < len(num_list):
            if ( num_list[i] + 1 == num_list[i+1] ):
                continue
            else:
                ret = False
            i += 1

    return ret
    
# 2개의 숫자가 번갈아가며 나타날 때
def is_zigzag(num_list):
    l = len(num_list)
    a = num_list[0]
    b = num_list[1]
    if l == 3:
        if num_list[2] == a:
            return True
    elif l == 4:
        if num_list[2] == a and num_list[3] == b:
            return True
    elif l == 5:
        if num_list[2] == a and num_list[3] == b and num_list[4] == a:
            return True
    return False

# 숫자가 등차 수열을 이룰 때
def delta_is_n(num_list):
 
    d = num_list[1] - num_list[0] # 공차가 d
    l = len(num_list)
    if l == 3:
        if num_list[2] - num_list[1] == d:
            return True
    elif l == 4:
        if ( num_list[2] - num_list[1] == d ) and (num_list[3] - num_list[2] == d) :
            return True
    elif l == 5:
        if ( num_list[2] - num_list[1] == d ) and (num_list[3] - num_list[2] == d) and (num_list[4] - num_list[3] == d):
            return True
    return False

# 조잡해도 이게 빠를듯.

# 3, 4, 5로 나눌 때! 문자열이 딱 떨어져야 한다!
# 만약 문자열이 1, 2가 남으면 그 경우는 음의 무한대 반환?

# 최적 부분 구조를 만들려면 어떻게 하는게 좋을까?
# 남은 문자열을 입력!! 남은 문자열의 시작 인덱스를 입력하면 그에 해당하는 결과가 유일하고 외부요인에 독립적!
# 자연수는 8자리 이상 10,000자리 이하의 자연수이므로 cache의 인덱스는 크기는 




