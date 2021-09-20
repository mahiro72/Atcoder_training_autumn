N = int(input())
A = list(map(int,input().split()))
A2 = list(map(abs,A))

m,p,z=0,0,0

for a in A:
    if a>0:p+=1
    elif a<0:m+=1
    else:z+=1
    
ans = sum(A2)
if m%2==1:
    if z==0:
        ans-=2*(min(A2))

print(ans)