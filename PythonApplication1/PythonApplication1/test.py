from map import *
map=[[1,13,1,1],
     [22,32,2,2],
     [3,4,5,6]]

for i in range(0,2):
    a1=map[-1]
    a2=map[-2]
    for x in range(len(map)):
        a2[x] += min(a1[x], a1[x+1])
        print(a2)
    map.pop(-1)
    map[-1] = a2
print(map[0][0])
