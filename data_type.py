

#literal assignment
first_name="Karthika"
last_name="Dharmaraj"

print(type(first_name))
print(type(first_name)==str)
print(isinstance(first_name,str))

#concatenatin
full_name=first_name+" "+last_name
print(full_name)


#casting
decade= str(90)
print(type(decade))
sentance="I'm a "+decade+"s kid."
print(sentance)

#multiline
multiline= """
I can do it              
       tring my best!
 I did it      

 """
print(multiline)

#escaping special characters

sentance_2='i\'m back at work!\thi!\n\nwhere\'s this at\\located?'
print(sentance_2)

#string methods

print(first_name)
print(first_name.lower())
print(first_name.upper())
print(full_name.title())
print(full_name.capitalize())

print(multiline.replace("I","you"))
print(multiline)

print(len(multiline))

multiline+="             "
multiline="        "+multiline
print(multiline)
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#build a menu
title="menu".upper()
print(title.center(30,"*"))
print('')
print('coffee'.ljust(20,".")+"$1".rjust(5))
print('Masala tea'.ljust(20,".")+"$2".rjust(5))
print('Milk'.ljust(20,".")+"$3".rjust(5))


#string index
print(first_name[1])
print(first_name[-1])
print(first_name[1:-1])
print(first_name[0:])
print(first_name[:1])

#methods to return boolean data
print(first_name.startswith("K"))#case sensitive
print(first_name.endswith("a"))
#boolean data type

myvalue=True

print(type(myvalue))
print(isinstance(myvalue,bool))

#numeric data type
#integer type
price=30
print(type(price))
print(isinstance(price,int))

#float type

deci=1.2
print(type(deci))
print(isinstance(deci,float))

#complex type

comp=5+2j
print(type(comp))
print(comp.imag)
print(comp.real)

#build in number function

print(abs(deci))
print(round(deci))
print(round(deci,1))
import math

print(math.pi)
print(math.sqrt(4))
print(math.ceil(deci))
print(math.floor(deci))

#casting string to int
post_code='5884'# error if word to int
code_value=int(post_code)
print(type(code_value))


