def solve(x):
    f = [True]*(x+1)
    for i in range(2,x+1):
        if not f[i]:continue
        for j in range(2*i,x+1,i):
            f[j]=False
    r = []
    for i in range(2,x+1):
        if f[i]:r.append(i)
    return r

N = int(input())
x = 55555
l = solve(x)

ans = []
i = 0
while len(ans)<N:
    if l[i]%5==1:
        ans.append(l[i])
    i+=1

print(*ans)