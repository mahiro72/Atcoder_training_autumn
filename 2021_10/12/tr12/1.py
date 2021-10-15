H,W = map(int,input().split())
A = [list(map(lambda c:1 if c=='+'else -1,input()))for _ in range(H)]
dp = [[0]*W for _ in range(H)]
INF = 10**9

for i in reversed(range(H)):
    for j in reversed(range(W)):
        if i==H-1 and j==W-1:continue
        if (i+j)%2==0:
            dp[i][j] = -INF
            if i+1<H:dp[i][j] = max(dp[i][j],dp[i+1][j]+A[i+1][j])
            if j+1<W:dp[i][j] = max(dp[i][j],dp[i][j+1]+A[i][j+1])
        else:
            dp[i][j] = INF
            if i+1<H:dp[i][j] = min(dp[i][j],dp[i+1][j]-A[i+1][j])
            if j+1<W:dp[i][j] = min(dp[i][j],dp[i][j+1]-A[i][j+1])

ans = dp[0][0]
print('Takahashi' if ans>0 else 'Aoki' if ans<0 else 'Draw')

