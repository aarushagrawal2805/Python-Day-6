class Calculator:
    def add(self, a, b):
        return a + b # This is called a abstract method bcz user do not show how addition is performing in calc,User only get output not process

calc = Calculator()
print("Addition is :",calc.add(10, 20))
