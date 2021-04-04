'''
     - 3 -
1 - 0      4
     - 2 - 

'''
# 인접행렬
n = 5
d = [ [0 for i in range(n) ] for j in range(n) ] 

d[0][1] = d[1][0] = 1
d[0][3] = d[3][0] = 1
d[0][2] = d[2][0] = 1
d[3][4] = d[4][3] = 1
d[2][4] = d[4][2] = 1

for i in range(n):
    print(d[i])


# 인접리스트
l = [ [] for i in range(n) ] # number of vertex = n
l[0].append(1)
l[0].append(2)
l[0].append(3)

l[1].append(0)

l[2].append(0)
l[2].append(4)

l[3].append(0)
l[3].append(4)

l[4].append(2)
l[4].append(3)


for i in range(n):
    print(i, l[i])
