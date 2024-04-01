import sys

a=input("Enter the first number: ")
b=input("Enter the second number: ")
c=input("Enter 1 to add \n Enter 2 to sub \n Enter 3 to mul \n Enter 4 to div \n  ")
a1=int(a)
b1=int(b)
c1=int(c)
if c1==0 and  c1>4:
    sys.exit("Invalid operation enter 1,2,3,or 4")

if c1==1:
    print(a,'+',b, '=',a1+b1)
elif c1==2:
    print(a,'-',b,'=',a1-b1)
elif c1==3:
    print(a,'*',b,'=',a1*b1)
elif c1==4:
    print(a,'/',b,'=',a1/b1)
