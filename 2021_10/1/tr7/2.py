from collections import deque

H,W = map(int,input().split())
g = [input() for _ in range(H)]

INF = 10**7
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
        
def bfs(sx,sy):
    global visited
    d = deque()
    d.append((sx,sy))
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    visited[sy][sx]=0
    while d:
        x,y = d.popleft()
        sec = visited[y][x]+1
        for dx,dy in move:
            if 0<=x+dx<W and 0<=y+dy<H:
                if g[y+dy][x+dx] != "#" and sec<visited[y+dy][x+dx]:
                    visited[y+dy][x+dx]= sec
                    d.append((x+dx,y+dy))
        if g[y][x] in alpha:
            for nx,ny in t[g[y][x]]:
                if sec<visited[ny][nx]:
                    visited[ny][nx] = sec
                    d.append((nx,ny))
            t[g[y][x]].clear()
            
        
bfs(sx,sy)

print(visited[gy][gx] if visited[gy][gx]!=INF else -1)

