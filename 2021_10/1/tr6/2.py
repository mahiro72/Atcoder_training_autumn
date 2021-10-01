N,T = map(int,input().split())
ab = [list(map(int,input().split()))for _ in range(N)]
ab.sort(key=lambda x:x[0])

dp = [[0]*(T+1)for _ in range(N+1)]
ans = 0

for i,(a,b) in zip(range(1,N+1),ab):
    for j in range(T):
        dp[i][j] = dp[i-1][j]
        ans = max(ans,dp[i][j]+b)
        if j>=a:
            dp[i][j] = max(dp[i][j],dp[i-1][j-a]+b)

# print(dp[N])
print(ans)
