squared=lambda num:num*num
#squared=lambda num:num*num
print(squared(3))
add10=lambda a:a+10
print(add10(2))
sum_total=lambda a,b:a+b
print(sum_total(3,2))
#########################
#higher order funtion
numbers=[1,2,3,4,5,6]

sqr_numbers=map(lambda num:num*num,numbers)
print(list(sqr_numbers))

odd_numbers=filter(lambda num :num%2!=0,numbers)
print(list(odd_numbers))

from functools import reduce
total= reduce(lambda a,b:a+b,numbers)
print(total)
print(sum(numbers))#sum is a built in funtion
names=["arun","kartika","ananya","advaitha","god"]
num_of_char=reduce(lambda a,b:a+len(b),names,0)
print(num_of_char)
