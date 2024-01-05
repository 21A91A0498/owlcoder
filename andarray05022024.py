arr = list(map(int,input().split()))
# for i in range(3):
#     l,r = map(int,input().split())
#     c = arr[l]
#     for j in range(l+1,r+1):
#         c&=arr[j]
#     print(c)
l = []
for i in range(len(arr)):
    l.append([0]*32)
for i in range(len(arr)) :
    c = -1 # pos
    n = 1 # 
    k= 32
    while k :
        p = arr[i]&n
        arr[i]>>=1
        if i>0:# 1
            l[i][c] = p+l[i-1][c] # 1 + 1
            c-=1
        else:
            l[i][c] = p
            c-=1
        k-=1
print(l)
for i in range(3):
    L,r = map(int,input().split())
    if L == 0 :
        k = r+1
        c = 0 
        two=0
        for i in range(31,-1,-1):
            if l[r][i] == k:
                two+=2**c
            c+=1
        print(two)
    else:
        c = 0 
        two = 0
        for i in range(31,-1,-1):
            # print(l[r][i],l[L-1][i])
            # break
            if l[r][i]-l[L-1][i] == r-L+1:
                two+=2**c
            c+=1
        print(two)
                
            
        
        

        

        
        
        