s=input()
a=s[0]
n=s[1]
b=s[2]
c=s[4]
if n=='-' and a=='x':
    x=int(c)+int(b)
elif n=='+' and a=='x':
    x=int(c)-int(b)
elif n=='-' and b=='x':
    x=int(a)-int(c)
elif n=='+' and b=='x':
    x=int(c)-int(a)
elif n=='-' and c=='x':
    x=int(a)-int(b)
elif n=='+' and c=='x':
    x=int(a)+int(b)
print(x)