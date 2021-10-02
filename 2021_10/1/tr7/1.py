N = int(input())

def f(x):
    r = []
    while x%2==0:
        x//=2
        r.append(2)
    tmp = 3
    while x!=1:
        if x%tmp==0:
            r.append(tmp)
            x//=tmp
            continue
        tmp+=2
    return r

cnt = {x:0 for x in range(1,N+1)}

for i in range(1,N+1):
    for j in f(i):
        cnt[j]+=1

ans=1
mod = 10**9+7

for i in cnt.values():
    ans*=(i+1)%mod

print(ans%mod)