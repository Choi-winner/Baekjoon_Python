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
    wildcards.append(sys.stdin.readline())
    N = int(sys.stdin.readline())
    temp = []
    for j in range(N):
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




# 각 문자열의 일치 여부를 확인하는 함수.
# def match(w, s): # w는 wildcard pattern, s는 filename.
#     if cache[]
#     # 인덱스를 하나하나 이동시키며 일치여부를 확인한다. 
#     # w의 원소에 ?가 있으면 일치한다고 판단한다.
#     # w의 원소에 *이 나오면 거기서부터 끝까지의 새로운 w', s'를 만들어서 재귀로 넘긴다.
#     pos = 0
#     while (pos < len(w)) and (pos < len(s)) and (w[pos] == '?' and w[pos] == s[pos]):
#         pos += 1
    
    
    






