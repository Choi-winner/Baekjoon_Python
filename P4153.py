'''
문제
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 
직각 삼각형인것을 알아냈다. 
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력
입력은 여러개의 테스트케이스로 주어지며 
마지막줄에는 0 0 0이 입력된다. 
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며,
각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 
"right", 아니라면 "wrong"을 출력한다.
'''
triangles = []
results = []
while True:
    input_string = input()
    if input_string == '0 0 0':
        break
    triangles.append(input_string.split())
for tri in triangles:
    if pow(int(tri[0]),2) == pow(int(tri[1]),2) + pow(int(tri[2]),2):
        results.append('right')
        continue
    elif pow(int(tri[1]),2) == pow(int(tri[0]),2) + pow(int(tri[2]),2):
        results.append('right')
        continue
    elif pow(int(tri[2]),2) == pow(int(tri[1]),2) + pow(int(tri[0]),2):
        results.append('right')
        continue
    else:
        results.append('wrong')
for result in results:
    print(result)

# 개선 방안
# num = list(map(int,input().split()))
# 을 사용하면 초반에 입력받는 것을 간단하게 할 수 있고, 나중에 각각에 int를 안해도 된다.
# map(int, input().split()) 하면, input().split()한 결과인 list의 요소에 int 함수를 적용하여
# map변수 형태로 반환한다.
# 이것을 list로 감싸주면 list형이 출력된다.  
# 아래와 같다.
'''
string1 = '1 2 5'
map1 = map(int, string1.split())
print('map: ',map1) # map:  <map object at 0x0000000001E17B80>
list1 = list(map1)
print(list1) # [1, 2, 5]
'''