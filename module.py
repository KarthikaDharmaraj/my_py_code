from math import pi 
import sys
import random as rdm #  can use rdm insdead of random
import class_obj #coustume module

# print(pi)
# print (dir(sys))  # what is in the module as list
# for items in dir(rdm):
#     print(items)  # while do the same but more readable

print(__name__)
print(class_obj.__name__)

print(class_obj.arun.wife)
print(class_obj.dharma.wife)
print(class_obj.rajen.wife)