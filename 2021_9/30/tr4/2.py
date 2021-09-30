class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n
    
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.parents[x]>self.parents[y]:
            x,y = y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    


N,M = map(int,input().split())
ab = [list(map(int,input().split()))for _ in range(M)]

uf = UnionFind(N+1)
r = (N-1)*N//2

ans = []
for a,b in ab[::-1]:
    ans.append(r)
    if uf.find(a)!=uf.find(b):
        r-=uf.parents[uf.find(a)]*uf.parents[uf.find(b)]
    uf.union(a,b)

print(*ans[::-1],sep='\n')