S = input()
dic = {x:0 for x in ['a','b','c']}
for s in S:
    dic[s]+=1
print('YES'if max(dic.values())-min(dic.values())<=1 else 'NO')
