import math

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

# TASK 6.1
a,b=map(int,input("A B: ").split())
g=gcd(a,b)
print("GCD=",g)
print("LCM=",a*b//g)

# TASK 6.2
a,b,c,d,diag=map(int,input("a b c d diag: ").split())
p1=(a+b+diag)/2
s1=math.sqrt(p1*(p1-a)*(p1-b)*(p1-diag))
p2=(c+d+diag)/2
s2=math.sqrt(p2*(p2-c)*(p2-d)*(p2-diag))
print("Ploshad=",s1+s2)
