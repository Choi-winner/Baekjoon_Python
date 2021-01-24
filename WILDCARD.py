'''
예제 입력
2
he?p
3
help
heap
helpp
*p*
3
help
papa
hello
예제 출력
heap
help
help
papa


he?p 
-> 이거는 ? 자리는 아예 돈케어 해버리면 될듯.]
*p*
*이 앞에 있다면, p가 나올 때까지 문자열 앞부터 탐색.
p가 없다면 False
p가 나왔으면, 그 다음에는 그 다음 문자열이 일치하는지 탐색.
*이 나왔으면, *가 나오고 그 다음 
'''

# 입력을 받는 부분
import sys
C = int(sys.stdin.readline())
wildcards = []
filenames = []
for i in range(C):
    # wildcard = sys.stdin.readline()
    # wildcards.append(wildcard[0:-1])
    wildcards.append(sys.stdin.readline())

    N = int(sys.stdin.readline())
    temp = []
    for j in range(N):
        # name = sys.stdin.readline()
        # temp.append(name[0:-1])
        temp.append(sys.stdin.readline())
    filenames.append(temp)

# 입력을 확인하는 부분.    
for i in range(C):
    print(i+1,'번째 입력에 대한 출력')
    print('wildcard 명: ',wildcards[i])
    for name in filenames[i]:
        print('name: ',name)

# 문자열의 일치여부를 저장하는 list
# 문자열이 100의 길이 제한을 가지고 있으므로, 
# w와 s의 입력에 대한 출력은 101*101 = 10201개로 제한된다. 
# <- ??? 문자열이 각각 100의 길이를 가진다. 그러면 match함수의 입력의 경우의 수는 101
'''
입력된 W, S가 있다. 거기서 우리는 접미사만 뽑아서 w와 s로 만들어 match함수에 입력한다.
그러면 하나의 입력된 조합 W, S에 대하여 101*101개의 입력만을 가진다? 그건 이해함.
그러면 각 입력에 대해서 새로운 cache를 부여해야한다.
cache는 각 입력의 match 여부를 판단하고 없앤다?
이때, '각 입력'이라는 것은 W, S 한 쌍이다.
w, s 한 쌍은 match의 입력이고, 이건 cache를 가지지 않는다.
+ 궁금한 점2
w와 s를 시작위치만으로 입력한다는 것이 무슨의미?
아 W와 S를 기억하고 있으니깐, w, s가 W, S의 시작위치로 주어지면,
W[w], S[s]로 참조하면 되겠네.
그리고, 시작 위치는 cache의 인덱스가 될 수 있겠다.
'''
# cache = [[-1]*101]*101

def match_prime(w_prime, s_prime):
    cache = [[-1]*101]*101
    # 입력된 w_prime 과 s_prime의 시작 위치에 따른 접미사만 뽑아서 w, s를 만든다.
    # 각 문자열의 일치 여부를 확인하는 함수.
    def match(w, s): # w는 wildcard pattern, s는 filename.
        if cache[w][s] != -1: # 이것이 memoization.(한 번 들어왔던 입력이면 저장되어 있는 것 바로 출력.)
            return cache[w][s] # 항체같은 것.
        # 인덱스를 하나하나 이동시키며 일치여부를 확인한다. 
        # w의 원소에 ?가 있으면 일치한다고 판단한다.
        # w의 원소에 *이 나오면 거기서부터 끝까지의 새로운 w', s'를 만들어서 재귀로 넘긴다.
        pos = 0
        while (pos < len(w_prime) - w) and (pos < len(s_prime) - s) and (w_prime[w+pos] == '?' or w_prime[w+pos] == s_prime[s+pos]):
            pos += 1

        # 2가지만 확인하고, 나머지는 모두 False를 반환하면 된다.
        # 우선, 패턴의 끝에 도달해서 끝난 경우, 문자열도 함께 끝났는지 확인하고, 문자열도 끝났다면 True.
        # 패턴의 끝에 도달하지 않았는데, while문이 끝났으면 '*'을 만난 경우이다.
        # 패턴의 마지막 char이 '*'이라면 s의 몇 글자가 이 '*'에 대응해야할지 재귀호출을 통해 찾는다.
        # 몇 글자가 대응했는지는 skip이라는 정수형 변수에 입력한다.

        # 1. s가 끝났는데, w도 마침 끝이다. (일치하는 케이스)
        if pos == (len(w_prime) - w) and pos == (len(s_prime) - s):
            cache[w][s] = 1
            return 1 # 1이 True를 의미한다.
        # 2. s가 안끝났다면 이건 '*'을 만난 상황이다. return 이후이므로 elif나 else가 필요 없다.
        if w_prime[w+pos] == '*':
            skip = 0
            while s + pos + skip < len(s_prime):
                if match(w + pos + 1, s + pos + skip) == 1:
                    cache[w][s] = 1
                    return 1
                skip += 1
        # 나머지의 경우는 모두 False를 의미하는 0을 반환시킨다.
        cache[w][s] = 0
        # print('일치하지 않는데, 이 순간의 w,s:', w, s, 'pos:',pos)
        return 0


    temp = match(0, 0) # 최초 입력은 인덱스 (0, 0)

    if temp == 1:
        print(s_prime[0:-1])
        # print(w_prime, '과', s_prime, '의 매치 결과는 True')
        return True
    else:
        # print(w_prime, '과', s_prime, '의 매치 결과는 False')
        return False


print('-----Wildcard와 입력에 대한 일치여부-----')
# w_prime, s_prime을 입력하는 부분. (main과 같은 부분)
for i in range(C):
    ret = 0
    print(wildcards[i][0:-1],'와 일치하는 filename들은 다음과 같다.')
    for name in filenames[i]:
        if match_prime(wildcards[i], name):
            ret += 1   
    print(i+1,'번째 케이스에서 일치의 횟수는 ',ret)
    