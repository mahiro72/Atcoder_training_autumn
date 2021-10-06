H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

tmp = []
for i,a in enumerate(A):
    for j in range(a):
        tmp.append(i+1)

ans = []
for i in range(H):
    x = tmp[i*W:(i+1)*W]
    if i%2==1:x.reverse()
    print(*x)
