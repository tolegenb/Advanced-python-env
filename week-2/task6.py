def all_eq(l):
    max=0
    for i in l:
        d=len(i)
        if d>max:
            max=d
            
    x=[]
    for i in l:
        n=max-len(i)
        if n>0:
            i=i+"_"*n
        x.append(i)
    return x
    
y=int(input())
data = [input() for _ in range(y)]
print(*all_eq(data), sep='\n')