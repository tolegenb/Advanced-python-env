n=int(input())
alp="ABCEHKMOPTXY"
for _ in range(n):
    s=input()
    x=True
    if len(s)!=6:
        x=False
    elif s[0] not in alp:
        x=False
    elif not s[1].isdigit():
        x=False
    elif not s[2].isdigit():
        x=False
    elif not s[3].isdigit():
        x=False
    elif s[4] not in alp:
        x=False
    elif s[5] not in alp:
        x=False
    if x:
        print("Yes")
    else:
        print("No")