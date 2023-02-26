n=int(input())
s=0
a=1
while n>0:
    k=n%10
    n=n//10
    s=s+a*k
    a=a*2
print(s)