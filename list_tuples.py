users=["Arun","Karthika","Ananya","Advaitha"]

data=["god",111,True]

empty=[]

print("Arun" in users)
print("Arun" in data)
print(users[0])
print(users[-1])
print(users[:3])
print(users[1:3])
print(users[1:])
print(users.index("Ananya"))
users.append("Karthik")
data.clear()#only to delet entire list 
print(data)#after clear will get empty list as output

# users.insert()
users.extend(["Dharmaraj","Kalavathy"])#to add more then one data use [] 
users +=["Rajendran","Amutha"]
users.insert(0,"Kamalavalli")
users[1:1]=["I","Me","you"]#insert data in index 1
print(users)
users[1:4]=["Priya","Krishav","Sivam"]#replace data from index 1 to 4
print(users)
users.remove("Sivam")
print(users)
users.sort()#will sort alphabetical order case sensitive lower case at end
print(users)
users.reverse()
print(users)
data1=[3,4,5,6,2]
print(data1)
data2=list(data1)
data2.reverse()
print(data2)
#copy list
copydata1=data1.copy()
mycopy=list(data1)
print(copydata1)
print(mycopy)

#tubles cannot  modify the data
mytuple=(1,2,3,4)
nexttuple=tuple((1,2,3,4,5,6))
#to add data to tuble
newlist=list(mytuple)
newlist.append(9)
newtuple=tuple(newlist)
print(newtuple)
print(newlist)
#unpacking tuple
print(mytuple[1:3])#indexing is same as list
(a,b,*c)=mytuple
#values stored in order and all other will be in *
print(a)
print(b)
print(c)


