#single inheritance
class dad():
    def phone(self):
        print("Dad's phone")
class son(dad):
    def ipad(self):
        print("son's ipad")
s=son()
s.phone()#son can acess dad,but dad cannot access son
d=dad()
#d.ipad() cannot do this


#muliple inheritance
class dad1():
    def phone(self):
        print("Dad1's phone")

class mom1():
    def sweet(self):
        print("mom's sweet")
class son1(dad1,mom1):
    def ipad(self):
        print("son's ipad")
s1=son1()
s1.phone()
s1.sweet()


# hierarchical inheritance
class granddad():
    def tv(self):
        print("Grand dad's TV")
class dad2(granddad):
    def phone(self):
        print("Dad2's phone")


class son2(dad2):
    def ipad(self):
        print("son's ipad")
s2=son2()
s2.phone()
s2.tv()

#hybrid  inheritance when you use differnt inheritance then its hybrid
