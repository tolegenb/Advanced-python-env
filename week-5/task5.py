class Bank:
    def __init__(self,a,b=0):
        self.__a=a
        self.__b=b
    def add(self,x):
        if x>0:
            self.__b+=x
    def take(self,x):
        if x<=self.__b:
            self.__b-=x
    def show(self):
        return self.__b

x=Bank("Bekzat",500)
x.add(200)
x.take(100)
print(x.show())
