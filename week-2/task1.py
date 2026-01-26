x=input()
num=0

for i in range(len(x) - 4):
    y=x[i:i+5]
    if y==">>-->" or y=="<--<<":
        num+=1
print(num)