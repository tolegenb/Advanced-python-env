a=input()
b=input()
m=len(b)
v=[b[i:]+b[:i] for i in range(m)]
print(sum(1 for i in range(len(a)-m+1) if a[i:i+m] in v))