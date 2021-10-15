H,W = map(int,input().split())
S = [input() for _ in range(H)]
memo = [set()for _ in range(H+W-1)]
mod = 998244353

for h in range(H):
    for w in range(W):
        memo[h+w].add(S[h][w])

ans = 1
for i in memo:
    if 'B'in i and 'R'in i:ans*=0;break
    elif '.' in i and len(i)==1:ans*=2;ans%=mod
print(ans%mod)
