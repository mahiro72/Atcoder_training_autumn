N = int(input())
P = list(map(int,input().split()))

used = [0]*(N-1)
d = {x:0 for x in range(1,N+1)}
for i,p in enumerate(P):
    d[p]=i

ans=[]
for i in range(1,N+1):
    x,now = i,d[i]
    while now!=x-1:
        d[P[now-1]]+=1
        d[x]-=1
        P[now]=P[now-1]
        P[now-1]=x
        now-=1
        if used[now]==1:exit(print(-1))
        used[now]=1
        ans.append(now)

ans = list(map(lambda x:int(x)+1,ans))
if sum(used)==N-1:print(*ans,sep='\n')
else:print(-1)

# print(*ans,sep='\n' if sum(used)==N-1 else -1)