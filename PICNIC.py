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

# 재귀함수, 짝지을 수 있는 경우의 수를 세는 함수.
def searching_couple_cases(list_of_couples_remain, num_of_cases): 
    # 탈출조건: 짝 지을 수 있는 친구의 수가 0명
    if len(list_of_couples_remain) == 1:
        print('retrunning 1')
        return 1 # 탈출 케이스는 0개의 경우의 수. 경우의 수가 1개.
    elif len(list_of_couples_remain) == 0: # 안쓰이는 경우인가?
        return 0
    else:
        for couple in list_of_couples_remain:
            # 한 커플을 꺼내고, 그 커플이 소속된 다른 couple들을 모두 list에서 지운다.
            list_of_couples_remain.remove(couple)
            a = couple[0]
            b = couple[1]
            print('a: ',a,'b: ',b)
            print('현재 리스트: ', list_of_couples_remain)
            for other_couple in list_of_couples_remain: # 뽑힌 커플이 속한 다른 커플을 모두 삭제한다.
                num_a = other_couple.count(a)
                num_b = other_couple.count(b)
                print('number of a and b: ',num_a, num_b)
                if num_a != 0 or num_b != 0:
                    print('removing this element: ', other_couple)
                    list_of_couples_remain.remove(other_couple)
            # num)of_cases에 1을 더한다.
            print('remainning couples: ', list_of_couples_remain)
            num_of_cases += searching_couple_cases(list_of_couples_remain, num_of_cases)
            print('num_of_cases: ', num_of_cases)
            return num_of_cases
    
# 입력 받는 부분.
TEST_CASES = int(sys.stdin.readline())

couples_listed = []*TEST_CASES
for i in range(TEST_CASES):
    N, C = map(int, (sys.stdin.readline()).split())
    # print('N, C', N, C)
    input_couples = sys.stdin.readline()
    input_couples = input_couples.split()
    # print('input_couples: ', input_couples)
    # print('length of input_couples: ', len(input_couples))
    temp_list = []
    for i in range(C):
        temp_list.append( [ input_couples[2*i], input_couples[2*i+1] ] ) # [ [0, 1], [1, 2], ... ]
    couples_listed.append(temp_list)
    # print('couples_listed: ', couples_listed)

print('couples_listed: ', couples_listed)
    

'''
1
2 1
0 1
'''
for i in range(TEST_CASES):
    # N, C = map(int, (sys.stdin.readline()).split())
    # input_couples = sys.stdin.readline()
    # input_couples.split()
    # print('input_couples: ', input_couples)
    # couples_listed = []
    # for i in range(C):
    #     couples_listed.append( [ input_couples[2*i], input_couples[2*i+1] ] ) # [ [0, 1], [1, 2], ... ]
    # print('couples_listed: ', couples_listed)
    print('couples_listed[i]: ',couples_listed[i])
    print(i,'번째 case의 결과: ', searching_couple_cases(couples_listed[i], 0))


