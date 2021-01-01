# P9020  
# 골드바흐의 추측
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다.
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 
# 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 
# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
# 이러한 수를 골드바흐 수라고 한다. 
# 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다. 

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다. (4 ≤ n ≤ 10,000)

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 
# 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다. 


# 소수를 만드는 함수.
def prime_maker(limit):
    num_list = list(range(2,limit))
    for n in num_list:
        for i in range(2,limit):
            if num_list.__contains__(n*i):
                num_list.remove(n*i) # n의 배수를 리스트에서 삭제한다.
            if n*i > limit:
                break # list에 있는 수가 아니면, 이 n에 대해서는 계산 끝
    return num_list

num_cases = input()
test_case = list(input() for _ in range(int(num_cases)))

prime_list = prime_maker(10000) # 입력되는 test 값에는 10000이상의 수가 없으므로

for even in test_case:
    one = int(int(even)/2)
    two = one
    for i in range(0,one): # 0을 빼는 것부터 시작해서, 1씩 증가시켜가며 빼고, 0에 도달할 때까지.
        if prime_list.__contains__(one) and prime_list.__contains__(two):
            print(f'{one} {two}')
            break
        else:
            one -= 1
            two += 1 # one과 two의 합은 항상 even으로 유지.
