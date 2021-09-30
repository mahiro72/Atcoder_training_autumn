
N = int(input())
A = list(map(int,input().split()))

P = [i+a for i,a in enumerate(A)]
Q = [j-a for j,a in enumerate(A)]

ans= 0

from collections import Counter
QC = Counter(Q)

for p in P:
    ans+=QC[p]
print(ans)
