class MyClass:

    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        if self.n <=40 :
         res = self.n
         self.n += 2
         return res
        else:
          print("Iteration is finised") #Stop Iteration
        raise StopIteration
    
even=MyClass() #Make object

for x in even:
   print(x)
