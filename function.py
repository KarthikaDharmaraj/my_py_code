# def hello():
#  print("hello world!")

# hello()
# def sum(num1,num2):
#  print(num1+num2)
# sum(1,2)
# def sub(a,b):
#  return a-b

# ans=sub(2,1)
# print(ans)
def multi_items(*args):
  print(args)
  print(type(args))

multi_items(1,2,3,4,5)
multi_items({1,2},3,4,5)
multi_items([1,2,3],4,5)
multi_items({1,2},{3,4,5})

def multi_named_items(**keyargs):
  print(keyargs)
  print(type(keyargs))

multi_named_items(one="ARUN",two="KARTHIKA")
multi_named_items(one=1,two=2,three=3)
multi_named_items(a="apple",two=2,three=3)
a=[1,2,3]
multi_items(a)