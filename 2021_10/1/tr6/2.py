N,T = map(int,input().split())
A,B=[],[]

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

n = []
dp = [[0]*(T+max(A)+1) for _ in range(N+1)]

for i,(a,b) in enumerate(zip(A,B)):
    for t in range(T+max(A)+1):
        dp[i+1][t] = dp[i][t]
        if a<=t<T+a:
            dp[i+1][t] = max(dp[i][t],dp[i][t-a]+b)

print(max(dp[N][T:]))
