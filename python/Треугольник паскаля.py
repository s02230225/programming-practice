a=[[0] for _ in range(105)]
for i in range(0,105):
    a[i]=[1]*i
#print(1,a[1])
#print(2,a[2])
for i in range(3,105):
    for j in range(1,i-1):
        a[i][j]=a[i-1][j-1]+a[i-1][j]
    #print(i,a[i])
b=a[102]
c=0
for i in range(len(b)):
    if b[i]%2==0: c+=1
print('ЧЁТНЫХ В',i,'СТРОКЕ',c)


n,m,d,k=map(int,input().split())
a=[[0 for i in range(m)] for j in range(n)]
b=[0 for _ in range(m)]
c=0
e=0
for i in range(k):
    x,y,z=map(int,input().split())
    a[x-1][y-1]=z
for i in range(m):
    for j in range(n):
        b[i]+=int(a[j][i])
for i in range(m-d+1):
    if c<sum(b[i:i+d]):
        c=sum(b[i:i+d])
        e=i
print(e+1)


a,b=map(int,input().split())
c=int(input())
d=[]
e=0
for i in range(c):
    x,y=map(int,input().split())
    d.append([x,y,x/y])
for i in range(len(d)):
    for j in range(len(d)-i-1):
        if d[j][2]>d[j+1][2]: d[j],d[j+1]=d[j+1],d[j]
b=b-a
for i in range(len(d)):
    e+=(b//d[i][1])*d[i][0]
    b=b%d[i][1]
if b==0: print(e)
else: print('NO')


count = dict()             
n = int(input())
for i in range(n):
    s = input()
    count[s] = count.get(s, 0) + 1
m = max(count.values())
for s in count:            
    if count[s] == m:       
        print(s)