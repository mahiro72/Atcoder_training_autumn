N,K = map(int,input().split())
V = list(map(int,input().split()))

ans = -float('inf')
for l in range(min(N,K)+1):
    for r in range(min(N-l,K-l)+1):
        s = V[:l]+V[-r:] if r>0 else V[:l]
        t = K-l-r
        tmp = sum(s)
        for i in sorted(s):
            if i<0 and t>0:
                tmp += -i
                t-=1
        ans = max(ans,tmp)

print(ans)