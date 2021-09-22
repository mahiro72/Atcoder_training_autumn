S = input()
K = int(input())

alpha = 'abcdefghijklmnopqrstuvwxyz'

ans = []

for i,s in enumerate(S):
    pos = len(alpha)-alpha.index(s)
    if s=='a':
        ans.append('a')
    elif K-pos<0:
        ans.append(s)
    else:
        ans.append('a')
        K-=pos

if K>0:
    ans[-1] = alpha[(alpha.index(ans[-1])+K)%len(alpha)]

print(''.join(ans))
