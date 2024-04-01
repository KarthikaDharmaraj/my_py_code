class phone():
    chargertype= "c-type"#class variable
    def __init__(self,b,p) :
      self.brand=b #instance var
      self.price=p

    def display(self):
       print("Brand : ",self.brand)       
       print("price : ",self.price)       
       print("charger type : ",self.chargertype) 

sam=phone("samsung","10000")      
mi=phone("Redmi","6000")      
tcl=phone("TCL","2000") 
sam.display()     
mi.display()     
tcl.display()     