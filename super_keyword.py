class a():
    def __init__(self) :
        print("A")
    def display(self):
        print("class A")
        
class b(a):
    def __init__(self) :
        super().__init__()
        print("B")
    def display(self):
        print("class B")
class c(b):
     def __init__(self) :
    #     super().__init__
        print("C")
     def display(self):
        
        print("class C")

#a=a()
b=b()
c=c()
