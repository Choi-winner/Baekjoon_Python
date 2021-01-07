'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# 입력 방법은 input() 말고 sys.stdin.readline()d 을 쓰는 법을 배워보자.

# Counting sort 알고리즘 배워보자.
''' 
O(n*log(n)) 의 복잡성을 가진 알고리즘.
절댓값이 1,000,000보다 작거나 같은 정수가 중복없이 입력된다. -1,000,000 ~ 1,000,000
입력되는 수의 개수는 맨 첫 줄에 입력된다. n = 1 ~ 1,000,000
'''

import sys
n = int(sys.stdin.readline())
output_list = []
for i in range(n):
    output_list.append(int(sys.stdin.readline()))

# sorted() 는 괄호 안에 들어간 list가 sort된 상태로 for문을 돌릴 수 있게 해준다.
for i in sorted(output_list):
    print(i)