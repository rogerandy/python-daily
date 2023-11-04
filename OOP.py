class calculate:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x+self.y

x=float(input("數字1:"))
y=float(input("數字2   "))


Calculate=calculate(x,y)
result=Calculate.add()
print(f"總和{result}")