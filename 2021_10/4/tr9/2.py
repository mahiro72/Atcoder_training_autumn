N = int(input())
mod = 998244353
ans = 0
for q in range(1,int(N**0.5)+1):
    ans += (N//q-q)//2+1
    ans%=mod
print(ans%mod)