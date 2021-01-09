'''
문제
배열을 정렬하는 것은 쉽다. 
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. 
N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
'''
import sys
n_str = (sys.stdin.readline())
n_list = list(n_str)
n_list.sort(reverse=True)
result_str = int(''.join(n_list))
print(result_str)
'''
join 메소드는 임의의 수의 문자열을 연결하며 
메소드가 호출된 문자열은 주어진 각 문자열 사이에
삽입됩니다. 빈 문자열인 문자열 ''은 list의 요소 사이에 삽입되는 str이다.
요소 사이에 공백을 추가하려면 ' '
'''
