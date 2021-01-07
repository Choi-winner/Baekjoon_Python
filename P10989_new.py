'''
원하는 새로운 counting sort.
output array는 남기되, counting array는 없애보자.
count하고 그 카운팅된 갯수만큼 output array에 바로바로 입력.
'''
# 1. 입력받는 파트.
import sys
n = int(sys.stdin.readline())

# 입력을 어딘가에 저장하지 않고 바로 입력된 것을 count하기!
output_array = [0]*10001 # counting만 저장할 list!
for i in range(n):
    output_array[int(sys.stdin.readline()) - 1] += 1
for i in range(10001):
    for j in range(output_array[i]):
        print(i+1)