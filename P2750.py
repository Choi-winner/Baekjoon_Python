'''
문제
N개의 수가 주어졌을 때, 
이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
n = int(input())
numbers = []
for i in range(n): # 입력 받는 부분.
    numbers.append(int(input()))

for left in range(n):
    for right in range(left+1, n):
        if numbers[left] > numbers[right]: # 왼쪽 수가 오른쪽 수보다 크면 자리바꿈
            temp = numbers[left]
            numbers[left] = numbers[right] # left에 새로운 값 입력하고 다시 시작.
            numbers[right] = temp 
for i in range(n):
    print(numbers[i])        

