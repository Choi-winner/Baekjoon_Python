'''
문제
Quantization (양자화) 과정은, 더 넓은 범위를 갖는 값들을 작은 범위를 갖는 값들로 근사해 표현함으로써 자료를 손실 압축하는 과정을 말한다. 
예를 들어 16비트 JPG 파일을 4컬러 GIF 파일로 변환하는 것은 RGB 색 공간의 색들을 4컬러 중의 하나로 양자화하는 것이고, 
키가 161, 164, 170, 178 인 학생 넷을 '160대 둘, 170대 둘' 이라고 축약해 표현하는 것 또한 양자화라고 할 수 있다.
1000 이하의 자연수들로 구성된 수열을 최대 S종류 의 값만을 사용하도록 양자화하고 싶다. 이 때 양자화된 숫자는 원래 수열에 없는 숫자일 수도 있다. 
양자화를 하는 방법은 여러 가지가 있다. 수열 1 2 3 4 5 6 7 8 9 10 을 2개의 숫자만을 써서 표현하려면,
 3 3 3 3 3 7 7 7 7 7 과 같이 할 수도 있고, 1 1 1 1 1 10 10 10 10 10 으로 할 수도 있다.
  우리는 이 중, 각 숫자별 오차 제곱의 합을 최소화하는 양자화 결과를 알고 싶다.
예를 들어, 수열 1 2 3 4 5 를 1 1 3 3 3 으로 양자화하면 오차 제곱의 합은 0+1+0+1+4=6 이 되고,
 2 2 2 4 4 로 양자화하면 오차 제곱의 합은 1+0+1+0+1=3 이 된다.
수열과 S 가 주어질 때, 가능한 오차 제곱의 합의 최소값을 구하는 프로그램을 작성하시오.
입력
입력의 첫 줄에는 테스트 케이스의 수 C (1 <= C <= 50) 가 주어진다. 각 테스트 케이스의 첫 줄에는 수열의 길이 N (1 <= N <= 100), 
사용할 숫자의 수 S (1 <= S <= 10) 이 주어진다. 그 다음 줄에 N개의 정수로 수열의 숫자들이 주어진다. 수열의 모든 수는 1000 이하의 자연수이다.
출력
각 테스트 케이스마다, 주어진 수열을 최대 S 개의 수로 양자화할 때 오차 제곱의 합의 최소값을 출력한다.

예제 입력
2
10 3
3 3 3 1 2 3 2 2 2 1
9 3
1 744 755 4 897 902 890 6 777

예제 출력
0
651



1
10 3
3 3 3 1 2 3 2 2 2 1
'''
INF = float('inf')

# 입력 받는 부분
import sys
C = int(sys.stdin.readline())
n_list = []
s_list = []
num_list = []
for i in range(C):
    n_s = sys.stdin.readline()
    n, s = map(int, n_s.split())
    n_list.append(n)
    s_list.append(s)
    temp = sys.stdin.readline()
    temp = temp.split()
    temp = list(map(int, temp))
    num_list.append(temp)


print('\n\n--------------연산 시작--------------\n\n')
# n_list가 필요할까?

# 주어진 문제를 작은 문제로 나누어 해결하자.
# 작은 문제는 남은 부분 수열과 지금까지 사용한 s의 리스트가 주어졌을 때, 남은 부분 수열에서 최소 오차 제곱의 합을 찾는 것!

# 어떤 수로 양자화할 지 결정하는 함수를 만들어보자.
# 양자화한 수가 필요한 것이 아니라, 양자화된 후의 error의 개수가 결국 필요하다. error는 위의 sum_error_square로 구하자.
def minError(sublist):
    # 사용된 s의 값이 필요없다! 어차피 오름차순이므로 s도 겹치지 않을 것이기 때문!
    sum_list = []

    start = min(sublist)
    end = max(sublist)
    i = 0
    sum_list = []
    
    for quantom in range(start, end+1): 
        sum = 0
        for num in sublist:
            sum += (num - quantom) ** 2
        sum_list.append(sum)
        i += 1
   
    return min(sum_list)


for i in range(C):
    input_list = num_list[i] # input_list는 양자화 시스템의 인풋이다.
    s = s_list[i] # s개만큼 양자화할 수 있다.

    # input should be sorted
    input_list.sort() # 오름차순.
        
    # memoization에 사용되는 cache의 크기는? (정렬된 input_list의 인덱스의 개수) x (최초 s의 개수) 이다. 
    cache = [ [-1]*(s+1) ]*(len(input_list) + 1) # cache[i][j] = "i번째 인덱스부터 시작하는 부분 수열, j개로 나눌 수 있는 경우" 의 최소 오차 제곱의 합.


    # 함수는 남은 수열의 시작 인덱스와 남은 s의 개수(사용할 수 있는 quantom의 개수 = 남은 수열을 분할하는 개수)를 받아서 최소 오차 제곱의 합을 반환한다.
    def quantize(index, remain_s):
        # print(cache)
        # 1. 메모이제이션
        if cache[index][remain_s] != -1: # remain_s 가 0인 케이스는 계산이 필요없기 때문에 s = 1을 0의 자리에 넣는다.
            print('-----------memoization 실행-----------')
            print('index: ',index,'/ remain_s: ', remain_s, '/ cache[index][remain_s]: ', cache[index][remain_s])    
    
            return cache[index][remain_s]

        # 2. 기저케이스
        if remain_s == 1:
            ret = minError(input_list[index:])
            cache[index][remain_s] = ret
            print('ret가 어떤 형식이길래? ret: ',ret )
            print('여기에서 remain_s가 1일때, ')
            print('index: ',index,'/ remain_s: ', remain_s, '/ cache[index][remain_s]: ', cache[index][remain_s])
            print('cache가 ', cache)
            return ret

        # 3. recursive part 
        ret = INF
        remain_length = n_list[i] - index

        # 남은 수열에서 선택하는 서브 수열은 모든 길이 전부 다. (하나의 수부터 시작해서 전체 수열까지.) 
        for n in range(1, remain_length):
            ret = min( ret, minError(input_list[index:index+n]) + quantize(index + n, remain_s - 1) )
        cache[index][remain_s] = ret
        print('index: ',index,'/ remain_s: ', remain_s, '/ cache[index][remain_s]: ', cache[index][remain_s])

        return ret

    print(i+1,'번째 입력의 양자화 결과: ',quantize(0, s))

