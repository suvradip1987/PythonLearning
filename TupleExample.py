countrylist = ['in', 'uk', 'usa', 12]


mytuple= (countrylist,2,3)
for item in mytuple:
    print(item)

lst= list(mytuple)
print(type(lst))
print(lst)
# Tuple cannot be changed
#TypeError: 'tuple' object does not support item assignment
#mytuple[0] =5

# to change tuple you need to convert tuple to list.

