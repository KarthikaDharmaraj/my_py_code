band={"vocals":"plant",
      "guitar":"page"
      }
band2=dict(vocals="plant",guitar="page")
print(band)
print(band2)
print(type(band))
print(type(band2))

#access values
print(band.get("vocals"))
print(band["vocals"])

#list all keys
print(band.keys())
#list all values
print(band.values())

#list of keys/values pairs as tuples

print(band.items())

print("guitar" in band)
print("vocals" in band)
print("music" in band)

# cange value for a key
band['vocals']="covaredale"
# add new items
band.update({"drums":"Ananya","bass":"JPJ"})
print(band)
#remove item
#print(band.pop("bass"))#value as output and remove

band["dance"]="Advaitha"
print(band)
# print(band.popitem())# remove last added item and prt as tuple 
# print(band)

#delete and clear
del band["bass"]
print(band)
#empty dictionaries
band2.clear()
print(band2)
#completle delete band2
del band2

# BAD copy dictionaries
# band2=band #create a referance
# print('Bad copy!')
# print(band)
# print(band2)
# band2['drums']='ana'
# print(band)

# GOOD copy
band2= band.copy()

band2['drums']='ana'
print(band)
print(band2)

band3=dict(band)
print(band3)
print(band)

#nested dictinary
Deepa={"Mom":"Kala","Dad":"Dharma"}
Arun={"Mom":"Amutha","Dad":"Rajendran"}

family={"Deepa":Deepa,
        "Arun":Arun}
print(family)
print(family["Deepa"]["Mom"])
print(family["Arun"]["Mom"])


 #set
num={1,2,3,4,5}
num1=set((1,2,3,4,5))
print(num)
print(num1)
print(type(num))
print(len(num))

# no duplicates(repeated data) allowed 
num3={5,6,1,2,3,3,4}
print(num3)#output in order and remove duplicate

#True=1 and False=0 
new={1,True,False,0,2,3,6,7}
print(new)
#cannot refer set element with index or key
#add new element
new.add(8)
num.update(new)
print(new)
print(num)
one={1,2,3,4,5}
two={1,2,3,9,6,7,8}
comb1_2=one.union(two)
print(comb1_2)

# Keep only DUPLICATES
one.intersection_update(two)
print(one)

# Keep everything except duplicates
one={1,2,3,4,5}
two={1,2,3,9,6,7,8}
one.symmetric_difference_update(two)
print(one)


