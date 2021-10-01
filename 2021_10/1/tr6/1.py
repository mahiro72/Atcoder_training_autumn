N,K = map(int,input().split())
A = list(map(int,input().split()))
l,s,ans=0,0,0
for r in range(N):
    s+=A[r]
    while s>=K and l<=r :
        ans+=N-r
        s-=A[l]
        l+=1
print(ans)