H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

tmp = ''
for i,a in enumerate(A):
    tmp+=str(i+1)*a

ans = []
for i in range(H):
    x = tmp[i*W:(i+1)*W]
    ans.append(x if i%2==0 else x[::-1])

for i in ans:print(*[x for x in i])
