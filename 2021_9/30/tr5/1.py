sx,sy,tx,ty = map(int,input().split())
dx = tx-sx
dy = ty-sy
print('R'*dx+'U'*dy+'L'*dx+'D'*dy+'D'+'R'*(dx+1)+'U'*(dy+1)+'LU'+'L'*(dx+1)+'D'*(dy+1)+'R')