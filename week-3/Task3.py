import math
# TASK 3.1
a1,b1=map(int,input("Katety 1: ").split())
a2,b2=map(int,input("Katety 2: ").split())

h1=math.sqrt(a1*a1+b1*b1)
h2=math.sqrt(a2*a2+b2*b2)

print("Gipotenuzy:",h1,h2)

# TASK 3.2
s=input("Vvedite stroku: ").split()
for w in s:
    print("".join(sorted(w)),end=" ")
