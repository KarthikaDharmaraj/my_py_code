value=0
# while value<10:
#     value+=1
#     if value==5:
#         break
#     print(value)
while value<10:
    value+=1
    if value<=5:
        print(value)
    elif value==8:
        continue
    else:
        print("no")
    
        
else:
    
   print("Now the value is "+ str(value))

# #for loop
# names=["karthika","Arun","Ananya","Advaitha"]

# for x in names:
#     if x=="Ananya":
#         continue
#     print(x)

# for x in "OMNAMASIVAYA":
#     print(x)

# for x in range(10):
#     print(x)

# for x in range(5,10):
#     print(x)

# for x in range(5,100,5):
#     print(x)


#

names=["karthika","Deepa"]
duties=["love","pray","Eat","Repeat"]

# Nestes for

for name in names:
    for duty  in duties:
        print((name+" "+duty+ "."))
else:
    print("end")