'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 
아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

입력
첫째 줄에 단어의 개수 N이 주어진다. 
(1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
'''
import sys
from collections import Counter

n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(sys.stdin.readline())

# words에 있는 단어들의 갯수 세고 분류 
def ordering_count(words_in):
    c = list(Counter(words_in))

    for i in range(len(c)):
        c[i] = ''.join(list(c[i])[:-1]) # 단어 맨 뒤에 붙은 \n 제거.
    print(c)

    c_counted = {}
    for c_element in c: # ['no', 'more', 'but', ... ]
        c_counted[c_element] = len(c_element) 
        # c_counted = {'but': 3, 'i': 1, 'wont': 4, 'hesitate': 8, 'no': 2, ...}
    print(c_counted)
    max_length = max(c_counted.values())
    for length in range(1, max_length+1):
        # 각 length를 value로 가지는 key들을 list로 불러오고, sort를 통해 사전식으로 정렬하여 출력
        sub_list = []
        for word, count in c_counted.items():
            if count == length:
                sub_list.append(word)
        sub_list.sort()
        for i in sub_list:
            print(i)



ordering_count(words)