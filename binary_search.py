# n, k
# n은 주어지는 수 리스트의 길이. <- 이 n개의 수가 오름차순으로 주어진다!!
# k는 찾아야하는 수. k가 n개의 수 중에 있으면 1 반환.

import sys
n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split())) # len(l) == n, l은 오름차순

def binary_search(l, k): # list l에서 k를 찾자.
    # base case: 1 혹은 2의 길이를 가지는 list에 k가 존재.
    lengh_of_l = len(l)
    if lengh_of_l <= 2:
        for num in l:
            if num == k:
                return True
        print('false인 지금 l: ', l)
        return False

    if lengh_of_l&2 == 0: # l의 길이가 짝수일 경우
        mid_index = int(lengh_of_l/2)
    else: # l의 길이가 홀수인 경우
        mid_index = int((lengh_of_l+1)/2)

    print('현재 list: ', l)
    print('mid index: ', mid_index)

    if l[mid_index] <= k: # mid_index보다 오른쪽에 k가 존재.
        list_left = l[mid_index:]
        return binary_search(list_left, k)
    else: 
        list_right = l[:mid_index-1]
        return binary_search(list_right, k)
 
if binary_search(l ,k) == True:
    print('k is in the list')
else:
    print('sorry it isn\'t here')