def funct(a):
    sum=0
    while(a>0):
        sum+=a%10
        a=a//10
    if sum<10:
        return sum
    else:
        return funct(sum)

for t in range(int(input())):
    a,n=map(int,input().split())
    a=funct(a)
    z=n%6
    if a==3 or a==6 or a==9:
        if n==1:
            print(a)
        else:
            print(9)
    else:
        ans=a**z
        ans=funct(ans)
        print(ans) 
