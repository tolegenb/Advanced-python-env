def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

# TASK 4.1
A,B,C,D=map(int,input("A B C D: ").split())
num=A*D
den=B*C
g=gcd(num,den)
print(num//g,"/",den//g)

# TASK 4.2
x,y,r=map(int,input("x y R: ").split())
points=[(1,2),(3,3),(10,2)]
cnt=0
for p in points:
    if (p[0]-x)**2+(p[1]-y)**2<=r*r:
        cnt+=1
print("Vnutri kruga:",cnt)
