n,m=map(int,input().split())
x=input()
ber={x[i:i+m] for i in range(n-m+1)}
print(len(ber))