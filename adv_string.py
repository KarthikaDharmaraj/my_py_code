person="Deepa"
coins=5
print("\n"+person+" has "+str(coins)+" coins left.")

#same output
print("\n%s has %s coins left."%(person,coins))
#format method
message=("\n{} has {} coins left.".format(person,coins))
print(message)
message=("\n{1} has {0} coins left.".format(person,coins))
print(message)
message=("\n{0} has {1} coins left.".format(person,coins))
print(message)
message=("\n{person} has {coins} coins left.".format(person=person,coins=coins))
print(message)
player={"person":"Deepa","coins":5}

message=("\n{person} has {coins} coins left.".format(**player))
print(message)

######################
# f stiring
message=f'\n {person} has {coins} coins left.'
print(message)
message=f'\n {person.lower()} has {coins*8} coins left.'
print(message)
message=f'\n {player["person"]} has {coins*2} coins left.'
print(message)

#####################
# you can pass formating option
num =10
print(f"2.25 times{num} is{2.2531*num}\n")#will give 2 decicemal value
print(f"2.25 times{num} is{2.2531*num:.2f}\n")

for num in range(1,11):
   print(f"2.25 times{num} is{2.2531*num:.2f}\n")
for num in range(1,11):
   print(f"{num} divide by 4052 is{2.2531*num:.2%}\n")
