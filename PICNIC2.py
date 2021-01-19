'''
문제
안드로메다 유치원 익스프레스반에서는 다음 주에 율동공원으로 소풍을 갑니다. 원석 선생님은 소풍 때 학생들을 두 명씩 짝을 지어 행동하게 하려고 합니다. 그런데 서로 친구가 아닌 학생들끼리 짝을 지어 주면 서로 싸우거나 같이 돌아다니지 않기 때문에, 항상 서로 친구인 학생들끼리만 짝을 지어 줘야 합니다.
각 학생들의 쌍에 대해 이들이 서로 친구인지 여부가 주어질 때, 학생들을 짝지어줄 수 있는 방법의 수를 계산하는 프로그램을 작성하세요. 짝이 되는 학생들이 일부만 다르더라도 다른 방법이라고 봅니다. 예를 들어 다음 두 가지 방법은 서로 다른 방법입니다.
(태연,제시카) (써니,티파니) (효연,유리)
(태연,제시카) (써니,유리) (효연,티파니)
입력
입력의 첫 줄에는 테스트 케이스의 수 C (C <= 50) 가 주어집니다. 각 테스트 케이스의 첫 줄에는 학생의 수 n (2 <= n <= 10) 과 친구 쌍의 수 m (0 <= m <= n*(n-1)/2) 이 주어집니다. 그 다음 줄에 m 개의 정수 쌍으로 서로 친구인 두 학생의 번호가 주어집니다. 번호는 모두 0 부터 n-1 사이의 정수이고, 같은 쌍은 입력에 두 번 주어지지 않습니다. 학생들의 수는 짝수입니다.
출력
각 테스트 케이스마다 한 줄에 모든 학생을 친구끼리만 짝지어줄 수 있는 방법의 수를 출력합니다.
'''
import sys

# 한 조각은 "아직 짝을 찾지 못한 학생을 짝지어 주는 것."
# 작은 문제: 아직 짝을 찾지 못한 학생들의 명단이 주어질 때, 친구인 학생들끼리 짝을 짓는 경우의 수를 구하라.

def count_Couple_Cases(list_of_matched, list_of_friends, Number_of_students):
    # 남은 학생 중 가장 번호가 빠른 학생을 찾는다. <- 중복을 제거하기 위하여 순번이 가장 빠른 학생부터 짝을 찾아준다.
    firstFree = -1
    for i in range(Number_of_students):
        if list_of_matched[i] is False:
            firstFree = i # 가장 빠른 순번의 매치되지 않은 학생.
            break

    # 기저 사례: 모든 학생이 매치되었으면 1을 반환.
    if False not in list_of_matched: # 모두 True인 경우.
        return 1 # 종료

    ret = 0
    # 친구이고, match되지 않은 학생끼리 매치시킨다.
    for i in range(firstFree+1, Number_of_students):
            if (list_of_friends[firstFree][i] is True) and (list_of_matched[firstFree] is False) and (list_of_matched[i] is False) and (i != firstFree):
                # 매치시킨다.
                list_of_matched[firstFree] = True
                list_of_matched[i] = True
                # print(i,'와',j,'가 matched')
                ret += count_Couple_Cases(list_of_matched, list_of_friends, Number_of_students) # ret를 이 경우에 1 증가시킨다.
                # 새로 입력된 list_of_matched에는 True가 2개 추가되었다.
                list_of_matched[firstFree] = False # 다시 False로 고치는 이유:
                list_of_matched[i] = False
    return ret # 모든 경우의 수를 계산한 결과를 return


#입력 받는 부분
TEST_CASES = int(sys.stdin.readline())

couples_listed = []*TEST_CASES
N_list = [] 
C_list = []
for i in range(TEST_CASES):
    N, C = map(int, (sys.stdin.readline()).split())
    # print('N, C', N, C)
    N_list.append(N)
    # C_list.append(C)
    input_couples = sys.stdin.readline()
    input_couples = input_couples.split()
    # print('input_couples: ', input_couples)
    # print('length of input_couples: ', len(input_couples))
    temp_list = []
    for i in range(C):
        temp_list.append( [ input_couples[2*i], input_couples[2*i+1] ] ) # [ [0, 1], [1, 2], ... ]
    couples_listed.append(temp_list)


'''
couples_listed[0] = [ [0, 1] ]
couples_listed[1] = [ [0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3] ]
couples_listed[2] = [  ]

'''

for i in range(TEST_CASES):
    
    has_matched = [False]*N_list[i] # 짝을 찾았으면 True로 바꾼다.

    areFriends = [ [False] * N_list[i] ] * N_list[i] # areFriends[i][j] = True이면 i와 j는 친구인 것.   

    for couple in couples_listed[i]: # 친구 쌍의 갯수만큼
        a = int(couple[0])
        b = int(couple[1])
        areFriends[a][b] = True
        areFriends[b][a] = True
    print(i+1,'번째 결과는 ',count_Couple_Cases(has_matched, areFriends, N_list[i]))