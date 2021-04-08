N=int(input())
s=[]
for i in range(N):
    s.append([])
for i in range(N):
    a=list(input().split())
    for j in range(N):
        if a[j]=='D':
            s[i].insert(j,0)
        elif a[j]=='F':
            s[i].insert(j,1)
        else:
            l=[0,0,0,0]
            for k in range(len(a[j])):
                if a[j][k]=='S':
                    l[0]=1
                elif a[j][k]=='E':
                    l[1]=1
                elif a[j][k]=='N':
                    l[2]=1
                elif a[j][k]=='W':
                    l[3]=1
            s[i].insert(j,l)
count=0
#NORTH
for k in range(N):
    stack=[]
    stack.append([0,k])
    i=0
    j=k
    flag=1
    t=k+2
    while(flag):
        #print(stack)
        if s[i][j]==0:
            stack.pop()
            if len(stack)!=0:
                i=stack[-1][0]
                j=stack[-1][1]
            else:
                flag=0
        else:       
            if s[i][j]==1:
                count=count+1
                flag=0
            elif(s[i][j][0]!=0 and s[i][j][0]<t):
                d=t-s[i][j][0]
                s[i][j][0]=s[i][j][0]+d
                i=i+1
                j=j
                stack.append([i,j])
            elif(s[i][j][1]!=0 and s[i][j][1]<t):
                d=t-s[i][j][1]
                s[i][j][1]=s[i][j][1]+d
                i=i
                j=j+1
                stack.append([i,j])
            elif(s[i][j][2]!=0 and s[i][j][2]<t):
                d=t-s[i][j][2]
                s[i][j][2]=s[i][j][2]+d
                i=i-1
                j=j
                stack.append([i,j])
            elif(s[i][j][3]!=0 and s[i][j][3]<t):
                d=t-s[i][j][3]
                s[i][j][3]=s[i][j][3]+d
                i=i
                j=j-1
                stack.append([i,j])
            else:
                stack.pop()
                if len(stack)!=0:
                    i=stack[-1][0]
                    j=stack[-1][1]
                else:
                    flag=0
#WEST
for k in range(1,N):
    stack=[]
    stack.append([k,0])
    i=k
    j=0
    flag=1
    t=t+1
    while(flag):
        #print(stack)
        if s[i][j]==0:
            stack.pop()
            if len(stack)!=0:
                i=stack[-1][0]
                j=stack[-1][1]
            else:
                flag=0
        else:       
            if s[i][j]==1:
                count=count+1
                flag=0
            elif(s[i][j][0]!=0 and s[i][j][0]<t):
                d=t-s[i][j][0]
                s[i][j][0]=s[i][j][0]+d
                i=i+1
                j=j
                stack.append([i,j])
            elif(s[i][j][1]!=0 and s[i][j][1]<t):
                d=t-s[i][j][1]
                s[i][j][1]=s[i][j][1]+d
                i=i
                j=j+1
                stack.append([i,j])
            elif(s[i][j][2]!=0 and s[i][j][2]<t):
                d=t-s[i][j][2]
                s[i][j][2]=s[i][j][2]+d
                i=i-1
                j=j
                stack.append([i,j])
            elif(s[i][j][3]!=0 and s[i][j][3]<t):
                d=t-s[i][j][3]
                s[i][j][3]=s[i][j][3]+d
                i=i
                j=j-1
                stack.append([i,j])
            else:
                stack.pop()
                if len(stack)!=0:
                    i=stack[-1][0]
                    j=stack[-1][1]
                else:
                    flag=0
print(count)

            
            
      
                
