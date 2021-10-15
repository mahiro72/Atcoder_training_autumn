N = int(input())
A,B = [],[]
for  i in range(N):
    a,b, = map(int,input().split())
    A.append(a)
    B.append(a+b)

d = {x:0 for x in sorted(list((set(A)|set(B))))}
for a,b in zip(A,B):
    d[a]+=1
    d[b]-=1

ans = [0]*(N+1)
cnt = 0
pre_date = 0
for now_date,n in d.items():
    ans[cnt]+=(now_date-pre_date)
    pre_date = now_date
    cnt+=n
print(*ans[1:])
