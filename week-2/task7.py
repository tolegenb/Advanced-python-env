a=input().split()
d={}
for x in a:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print("Purchase frequency:")
for x in d:
    print(x+":",d[x])
max_a = max(d,key=d.get)
print("\nMost popular item:",max_a)
y=[x for x in d if d[x]==1]
print("Purchased once:", " ".join(y))

print("\nSorted by frequency:")
for x in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(x[0], x[1])