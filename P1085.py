# P1085
# 직사각형에서 탈출.
'''
문제
한수는 지금 (x, y)에 있다. 
직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 
오른쪽 위 꼭짓점은 (w, h)에 있다. 
직사각형의 경계선까지 가는 거리의 최솟값을 구하는
프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.

제한
1 ≤ w, h ≤ 1,000
1 ≤ x ≤ w-1
1 ≤ y ≤ h-1
x, y, w, h는 정수
''' 
# input = input()
# input_tuple = input.split(' ')
# x = int(input_tuple[0])
# y = int(input_tuple[1])
# w = int(input_tuple[2])
# h = int(input_tuple[3])
# d = min(x, w - x, y, h - y)
# print(d)



# split : str.split() 하면 기본적으로 띄어쓰기를 통해서 문자열을 자르고, 그 결과를 list로 반환.
#         str.split('_') 하면 '_'를 구분자로 써서 문자열을 자른다.
# map : list의 요소를 하나씩 받아와서 지정된 함수로 처리하고, 그 결과를 새로운 list로 반환한다.
#       new_list = map(int, ori_list) <- new_list에는 ori_list에 있었던 string 형식의 숫자들을 int함수를 통해 int형으로 변환한 list가 저장된다.
#       따라서, map은 반복문을 대신할 수 있다.

