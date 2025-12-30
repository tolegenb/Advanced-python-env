import math

# TASK 2.1
a=float(input("Storona shestiugolnika: "))
h=a*math.sqrt(3)/2
hex_area=6*(a*h/2)
print("Ploshad=",hex_area)

# TASK 2.2
for i in range(3):
    x=float(input("a: "))
    y=float(input("b: "))
    print("Ploshad pryamougolnika=",x*y)
