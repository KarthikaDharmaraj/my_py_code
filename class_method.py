class laptop():
   chargertype= "c-type"#class variable

   
   def __init__(self) :
      self.brand="" #instance var
      self.price=34

   #instance method
   def setprice(self,price):
      self.price=price

   def display(self):
       print("Brand : ",self.brand)       
       print("price : ",self.price)       
       print("charger type : ",self.chargertype) 

   @classmethod  #@mis decratores
   def changechargertype(cls):
      cls.chargertype="B type"
      print("charger type : ",cls.chargertype)
    
   @staticmethod
   def info():
      print("hello world")

hp=laptop()
hp.brand="HP"
hp.setprice(23000)
hp.display()
hp.changechargertype()
hp.display()
hp.info()
   

    
   
