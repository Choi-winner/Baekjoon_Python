'''
문제
0보다 크거나 같은 정수 N이 주어진다. 
이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''

n = int(input())
n_factorial = 1 # factorial을 사용하지 않고 직접 구현
for i in range(1,n+1):
    n_factorial *= i
print(n_factorial)

