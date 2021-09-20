import numpy as np
N,M = map(int,input().split())
x,y,z = (np.zeros(N)for _ in range(3))
for i in range(N):
    x[i],y[i],z[i] = map(int,input().split())
scores = [x+y+z,x+y-z,x-y+z,-x+y+z,x-y-z,-x+y-z,-x-y+z,-x-y-z]
ans = 0
for s in scores:
    s = sorted(s,reverse=True)
    ans = max(ans,sum(s[:M]))

print(int(ans))