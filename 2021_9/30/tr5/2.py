import sys 
sys.setrecursionlimit(10**6)

N = int(input())
uvw = [list(map(int,input().split()))for _ in range(N-1)]

g = [[]for _ in range(N+1)]
for u,v,w in uvw:
    g[u].append((v,w))
    g[v].append((u,w))

color = [-1]*(N+1)

def dfs(x,cost):
    color[x]=cost
    for nxt,c in g[x]:
        if color[nxt]==-1:
            dfs(nxt,(cost+c)%2)

dfs(1,0)
print(*color[1:],sep='\n')