N = int(input())
ans = 0

def f(x,flag):
    global ans
    if int(x)>N:return
    if flag==7:ans+=1
    f(x+str(7),flag|4)
    f(x+str(5),flag|2)
    f(x+str(3),flag|1)

f('7',4)
f('5',2)
f('3',1)

print(ans)
