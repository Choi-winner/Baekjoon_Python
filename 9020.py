# 골드바흐의 추측 문제.
# 에라토스테네스의 체와 바이너리 서치를 이용해서 풀이.

import sys
from math import sqrt

# eratosthenes thesis
# 자연수 n 이하의 모든 소수의 list를 반환.
def eratos(n):
    prime_list = []
    b = [ True for _ in range(n+1)] # 1 ~ n 까지의 자연수 리스트
    b[1] = False # 1 은 소수가 아니다.
    b[2] = True # 2 는 소수이다. 

    # 2 부터 시작해서 
    for i in range(2, int(sqrt(n))+1):
        if b[i]: # 소수이면, 그 수의 제곱부터 시작해서 모든 배수는 소수가 아니므로 False로 제거.
            for j in range(i**2, n+1, i):
                b[j] = False

    # prime list에 upload
    for i in range(2, len(b)): 
        if b[i]: # 소수인 것들을 prime_list에 업데이트
            prime_list.append(i)
    return prime_list
    

# binary search
# l: 입력 리스트(오름차순으로 정렬된), v: 찾고자하는 값.
def bs(l, v):
    le = 0 # index of left-most value of current window
    ri = len(l) - 1 
    while le <= ri: # 요기를 <= 로 해야지, 이걸 < 로 하면 틀린다!!
        mid = (le + ri) // 2
        if l[mid] == v:
            return True
        elif l[mid] < v:
            le = mid + 1
        else:
            ri = mid - 1
    return False


prime_list = eratos(10000)
# print(prime_list)


T = int(sys.stdin.readline())
for i in range(T):
    even_n = int(sys.stdin.readline()) # 짝수 주어짐
    # 이 주어진 짝수를 Binary search를 통해서 두 소수의 합으로 나타내고, 
    # 두 소수의 차가 최소가 되는 쌍을 찾는 것이 프로그램의 목적.
    ans = []
    for j in range(len(prime_list)):
        if len(ans) == 0: # 만약 ans에 아무것도 없다면, 
            if even_n > prime_list[j]:
                if bs(prime_list, even_n - prime_list[j]): # 두 소수의 합이 짝수인 두 소수를 찾았을 때,
                    ans = [prime_list[j], even_n - prime_list[j]] # 바로 두 소수를 ans에 업로드
        else: # 만약 ans에 어떤 값이 이미 존재한다면,
            if even_n > prime_list[j]:
                if bs(prime_list, even_n - prime_list[j]):
                    if abs(ans[0] - ans[1]) > abs(prime_list[j] - (even_n - prime_list[j])): # 두 소수의 차가 더 작은 것을 업로드
                        ans = [prime_list[j], even_n - prime_list[j]] # 이 두 수는 자동으로 오름차순인가?
    print(ans[0], ans[1])

     
    