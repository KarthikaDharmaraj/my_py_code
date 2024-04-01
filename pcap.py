#ques 1
print(2**3**2**1)
#ques 2
print("peter's sisters name is \"anna\"")
#q3
i=250
while len(str(i))>72:
    i*=2
else:
    i//=2
print(i)
#q4
n=0
while n<4:
    n+=1
    print(n,end=" ")
    
#q5
    
x=0
y=2
z=len("phython")
x=y>z
print(type(x))
print(x)

#q6
val=1
val2=0
val=val^val2
val2=val^val2
val=val^val2
print(val)

#q7
z,y,x=2,1,0
x,z=z,y
y=y-z
x,y,z=y,z,x
print(x,y,z)

#q8
a=0
b=a**0
print(b)

#q9
# i=10
# while i>0:
#     i-=3
#     print("*")
#     if i<=3:
#         break
# else:
#     print("*")

# q 10
    

for i in range(1,4,2):
    print("*")
for i in range(1,4,2):
    print("*",end="")
for i in range(1,4,2):
    print("*",end="**")
for i in range(1,4,2):
    print("*",end="**")
print("***")

# q12
x="20"
y="30"
print(x==y)

#q 13
a="hello, python!"
print(a[-14:15])

#q 14
lst=['a','b','c',2,4]
del lst[0:-2]
print(lst)

#q15
dict={"a":1,"b":2,"c":3}
for item in dict:
    print(item)
#q16
a="python"
for i in range(len(a)):
    i=a[i].upper()
print(a,end="")

#q17
# lst=[i//i for i in range(0,4)]
# sum=0
# for n in lst:
#     sum +=n
# print (sum)

a=3
def add(a):
   return a+2
a=2+add(a)
print(add(a))