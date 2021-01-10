'''
문제
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 
이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
입력은 가입한 순서로 주어진다.

출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 
나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
'''
import sys
# 1. [ [나이 str , 이름 str, 가입순서] , ... ] 로 저장하자.
n = int(sys.stdin.readline())
main_list = []
for i in range(n):
    list_element = sys.stdin.readline().split()
    list_element[0] = int(list_element[0])
    list_element.append(i+1)
    main_list.append(list_element) # [나이 str , 이름 str, 가입순서] append
print(main_list)

# 2. 나이 순으로 정렬하자.
main_list.sort(key=lambda x:x[0]) # 0번 인덱스에 있는 것이 나이. 나이 순 정렬.
print(main_list)

# 3. 나이의 최소 ~ 최대까지 for문 만들어서 나이가 같은 요소들로 sub list 만들자.
#    sub list에서 가입순서를 기준으로 다시 정렬해서 print.

# [age[0] for age in main_list] # main_list에서 0번째 인덱스만 뽑아오기.
ages = [age[0] for age in main_list]
for age in range(min(ages), max(ages)+1):
    sub_list = []
    for element in main_list:
        if age == element[0]: # 나이가 age[0]인 element 탐색.
            sub_list.append(element) # sub_list에 저장.
    for i in sub_list:
        print(i[0], i[1])