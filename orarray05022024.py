arr = list(map(int,input().split()))
l = []
for i in range(len(arr)):
    l.append([0]*32)

for i in range(len(arr)):
    n  = 32
    c = -1
    while n:
        p = arr[i]&1
        arr[i]>>=1
        if i>0:
            l[i][c] = p + l[i-1][c]
            c-=1
        else:
            l[i][c] = p
            c-=1
        n-=1
print(l)
for i in range(3):
    L,R = map(int,input().split())
    if L == 0 :
        c = 0 
        sum = 0 
        for i in range(31,-1,-1):
            if l[R][i]>0:
                sum+=2**c
            c+=1
        print(sum)
    else:
        c = 0 
        sum = 0 
        for i in range(31,-1,-1):
            if l[R][i]-l[L][i]>0:
                sum+=2**c
            c+=1
        print(sum)