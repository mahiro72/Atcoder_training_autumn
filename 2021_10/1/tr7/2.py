
# 2
from collections import deque
from itertools import combinations

H,W = map(int,input().split())
g = [input() for _ in range(H)]

INF = 10**5
visited = [[INF]*W for _ in range(H)]

alpha = 'abcdefghijklmnopqrstuvwxyz'
t = {x:[] for x in alpha}

sx,sy,gx,gy=0,0,0,0
for i in range(H):
    for j in range(W):
        if g[i][j]=="S":
            sx,sy = j,i
        elif g[i][j]=="G":
            gx,gy = j,i
        if g[i][j] in alpha:
            t[g[i][j]].append((j,i))
        
def bfs(sx,sy,x):
    global visited
    d = deque()
    d.append((sx,sy,x))
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    if visited[sy][sx]<x:
        return
    while d:
        x,y,sec = d.popleft()
        visited[y][x] = sec
        for dx,dy in move:
            if 0<=x+dx<W and 0<=y+dy<H:
                if g[y+dy][x+dx] != "#" and visited[y][x]+1<visited[y+dy][x+dx]:
                    d.append((x+dx,y+dy,sec+1))

bfs(sx,sy,0)

for al,xy in t.items():
    if len(xy)>=2:
        for (x1,y1),(x2,y2) in combinations(xy,2):
            # print(al,x1,y1,x2,y2)
            if visited[y1][x1]>=visited[y2][x2]:
                print(al)
                bfs(x2,y2,visited[y1][x1]+1)
            else:
                # print("#",al)
                bfs(x1,y1,visited[y2][x2]+1)



print(visited[gy][gx] if visited[gy][gx]!=INF else -1)

for i in visited:
    print(i)