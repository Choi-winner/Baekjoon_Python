''' 네 번째 점.
문제
세 점이 주어졌을 때, 
축에 평행한 직사각형을 만들기 위해서 
필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 
좌표는 1보다 크거나 같고, 
1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''

points = list(input() for _ in range(3)) # 3줄의 입력 str을 list에 저장.
x = []
y = []
xx = 0
yy = 0
for point in points:
    x1, y1 = map(int, point.split())
    x.append(x1)
    y.append(y1)
if x[0] != x[1] and x[0] != x[2]:
    xx = x[0]
elif x[0] != x[1] and x[1] != x[2]:
    xx = x[1]
elif x[1] != x[2] and x[0] != x[2]:
    xx = x[2]

if y[0] != y[1] and y[0] != y[2]:
    yy = y[0]
elif y[0] != y[1] and y[1] != y[2]:
    yy = y[1]
elif y[1] != y[2] and y[0] != y[2]:
    yy = y[2]

print(xx,yy)

