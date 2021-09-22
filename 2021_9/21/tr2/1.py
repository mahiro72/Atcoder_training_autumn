N,P = map(int,input().split())
A = list(map(int,input().split()))

odd = False
for a in A:
    if a%2:odd=True;break

if odd:
    print(pow(2,N-1))
else:
    print(0 if P==1 else pow(2,N))




# from math import comb

# N,P = map(int,input().split())
# A = list(map(int,input().split()))

# even,odd=0,0
# for a in A:
#     if a%2:odd+=1
#     else:even+=1

# def f(cnt,n):
#     tmp = 0
#     while n<=cnt:
#         tmp+=comb(cnt,n)
#         n+=2
#     return tmp


# if odd==0:
#     if P==1:
#         ans=0
#     else:
#         ans=pow(2,even)
# else:
#     if P==1:
#         ans = f(odd,1)*pow(2,even)
        
#     else:
#         ans = f(odd,0)*pow(2,even)


# print(ans)