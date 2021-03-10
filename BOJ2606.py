'''

1-2 
2-3 
1-5
5-2
5-6
4-7

1-2 -> 2-3





'''


import sys

C = int(sys.stdin.readline())
CC = int(sys.stdin.readline())

l = []
for i in range(CC):
	ll = list(map(int, sys.stdin.readline().split() ))
	l.append(ll)

# print(l) # [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

is_visited = [False for _ in range(C+1)]
# is_visited[i] = False이면, i번 컴퓨터에 방문하지 않은 것.
is_visited[1] = True
def dfs(l, n): # l: connections / n: current node.
	global is_visited
	for i in range(len(l)):
		a = l[i][0]
		b = l[i][1]
		if a == n and is_visited[b] == False:
			is_visited[b] = True
			dfs(l, b)
		if b == n and is_visited[a] == False:
			is_visited[a] = True
			dfs(l, a)
	return 

dfs(l, 1)

ans = -1 # 1번 컴퓨터도 방문한것이므로.
for tof in is_visited:
	if tof:
		ans += 1

print(ans)