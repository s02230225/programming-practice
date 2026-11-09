a=int(input())
b=[[0,1,0] for _ in range(a+1)]
for i in range(1,a+1):
    c=list(input())
    for j in 0,1,2:
        if c[j]=='.': b[i][j]=1
        elif c[j]=='C': b[i][j]=2
        else: b[i][j]=0
x=1
y=0    
while True:
    p1=0
    s1=0
    t1=True
    p2=0
    s2=0
    t2=True
    for i in range(1,a+1):
        if t1:
            if b[y+i][0]==0 and b[y+i][1]==0:
                t1=False
            elif b[y+i][0]==0 and b[y+i][1]==1:
                t1=False
            elif b[y+i][0]==0 and b[y+i][1]==2:
                s1+=1
                t1=False
            elif b[y+i][0]==1 and b[y+i][1]==0:
                p1+=1
            elif b[y+i][0]==1 and b[y+i][1]==1:
                t1=False
            elif b[y+i][0]==1 and b[y+i][1]==2:
                s1+=1
                t1=False
            elif b[y+i][0]==2 and b[y+i][1]==0:
                p1+=1
                s1+=1
            elif b[y+i][0]==2 and b[y+i][1]==1:
                p1+=1
                s1+=1
            elif b[y+i][0]==2 and b[y+i][1]==2:
                s1+=1
                t1=False
        if t2:
            if b[y+i][1]==0 and b[y+i][2]==0:
                t2=False
            elif b[y+i][1]==0 and b[y+i][2]==1:
                p2+=1
            elif b[y+i][1]==0 and b[y+i][2]==2:
                p2+=1
                s2+=1
            elif b[y+i][1]==1 and b[y+i][2]==0:
                t2=False
            elif b[y+i][1]==1 and b[y+i][2]==1:
                t2=False
            elif b[y+i][1]==1 and b[y+i][2]==2:
                p2+=1
                s2+=1
            elif b[y+i][1]==2 and b[y+i][2]==0:
                s2+=1
                t2=False
            elif b[y+i][1]==2 and b[y+i][2]==1:
                s2+=1
                t2=False
            elif b[y+i][1]==2 and b[y+i][2]==2:
                s2+=1
                t2=False                             
        if (not t1 and not t2) or i==a: break