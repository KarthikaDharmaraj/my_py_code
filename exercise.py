#exercise 1

# str = 'My Name is Jessa'
# list1=list (str.split(' '))
# #list2=list1.reverse()
# list2=[word[::-1] for word in list1]
# print(list1)
# print(list2)
# new_str=" ".join(list2)
# print(new_str)

#exercise 2
# str1="line1\nline2\nline3\nline4\nline5\n"
# print(str1)
# str2=str1.replace("\n"," ")
# print(str2)

#exercise 3
# list1=[10,20,30,40,50,60,70,80,90,100]
# count=0
# list_len=len(list1)

# while count<list_len:
#     if list1[count]>50:
#         del list1[count]
#         # count +=1
#         list_len=list_len-1
#     else:
#         count +=1

# print(list1)

#exercise 4

# a=int(input("Enter the first no:"))
# b=int(input("Enter the laast no:"))

# def printrance(a,b):
#     for i in range(a,b):
#         print(i)
#     else:
#         print(b)

    
# printrance(a,b)    


#ecercise 5

# def validate(username,password):
#     if username=="EMG" and password=="123":
#         return True
#     else:
#         return False

# u=input("Enter ur username: ").upper()
# p=input("Enter ur password: ")

# c=validate(u,p)
# print(c)

#excercise 6
# class god:
#     def __init__(self) -> None:
    
#       name=""
#     def printname(self):
#         print(self.name+" LOVES U ")

# a=god()
# a.name=input("Enter the object name u want to creat: ").upper()
# a.printname()

# exercise object

# class student:
#     def __init__(self):
#       name=""
#       regno=""
#     def print_info(self)  :
#        print("Name : ",self.name)
#        print("Reg no : ",self.regno)

# s1=student()
# s2=student()  
# s1.name= "Arun"   
# s1.regno="1234"
# s2.name= "Karthi"   
# s2.regno="1235"
# s1.print_info()
# s2.print_info()
#method 2
# 
# class calculater:
#     def add(self,a,b):
#         c=a+b
#         print(str(a),"+",str(b),"=", str(c))
#     def sub(self,a,b):
#         c=a-b
#  
list_num=[10,20,30,40,50,60,70,80]
num_lt_50=filter(lambda num: num<=50,list_num)
print(list(num_lt_50))

    
dic={"a":65,"b":23,"c":43}
#reverse mappin
new_dic={value:key for key,value in dic.items()}
print(new_dic)


sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
exist = {}
duplicates = []


for x in sample_list:
    if x not in exist:
        exist[x] = 1
    else:
        duplicates.append(x)
print(duplicates)
print(exist)