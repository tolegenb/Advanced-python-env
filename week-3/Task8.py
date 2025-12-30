# TASK 8.1
n=int(input("n: "))
for i in range(1,n+1):
    ok=True
    for d in str(i):
        if d=="0" or i%int(d)!=0:
            ok=False
    if ok:
        print(i)

# TASK 8.2
m=int(input("Razmer: "))
A=list(map(int,input("Massiv: ").split()))
print("Ishodnyi:",A)
A[0],A[-1]=A[-1],A[0]
print("Novyi:",A)
