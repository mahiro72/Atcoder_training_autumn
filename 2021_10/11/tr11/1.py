H,W = map(int,input().split())
S = [input()for _ in range(H)]

dp = [[float('inf')]*W for _ in range(H)]
dp[0][0] = (0 if S[0][0]=='.'else 1)

for i in range(H):
    for j in range(W):
        if S[i][j]=='.':
            if i-1>=0:
                dp[i][j] = min(dp[i-1][j],dp[i][j])
            if j-1>=0:
                dp[i][j] = min(dp[i][j-1],dp[i][j])
        else:
            if i-1>=0:
                if S[i-1][j]=='#':
                    dp[i][j] = min(dp[i-1][j],dp[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j])
            if j-1>=0:
                if S[i][j-1]=='#':
                    dp[i][j] = min(dp[i][j-1],dp[i][j])
                else:
                    dp[i][j] = min(dp[i][j-1]+1,dp[i][j])

print(dp[H-1][W-1])
