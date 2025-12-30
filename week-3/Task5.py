def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

# TASK 5.1
A,B,C,D=map(int,input("A B C D: ").split())
num=A*D-B*C
den=B*D
g=gcd(abs(num),den)
print(num//g,"/",den//g)

# TASK 5.2
n=int(input("Chislo: "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

