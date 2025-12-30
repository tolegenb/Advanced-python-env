import math
# TASK 1.1
r=float(input("Radius kruga: "))
print("Ploshad kruga=",math.pi*r*r)

a=float(input("a pryamougolnika: "))
b=float(input("b pryamougolnika: "))
print("Ploshad pryamougolnika=",a*b)

base=float(input("Osnovanie treugolnika: "))
h=float(input("Vysota: "))
print("Ploshad treugolnika=",base*h/2)

# TASK 1.2
for i in range(3):
    arr=list(map(int,input("Vvedite massiv: ").split()))
    print("Summa=",sum(arr))
    print("Srednee=",sum(arr)/len(arr))
