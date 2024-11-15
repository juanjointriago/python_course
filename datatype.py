# datatypes in python
# string in python
# "XXXXX"
# 'XXXXX'
# '''XXXXX'''
# """XXXXX"""
# when you use funtion print you can use single or double quotes
# type(variable) => return the type of the variable
# can you use a function inside function like this
print(type(100))
# for concat you can use + like this
# "Bye"_+_"_"+_"Babe"
print("Bye" + " " + "Babe")
noneData = None
print(type(noneData))  # None
# Numbers in python
print(type(100))  # integer
print(type(100.0))  # float

# Boolean in python Upper Cammel case
print(type(True))  # boolean
print(type(False))  # boolean

# List in python infear any type of data use [] can change
print(type([1, 2, 3, 4, 5]))  # list

#Tuples in python inmutable list can't change use ()
print(type((1, 2, 3, 4, 5)))  # tuple

#Dictionaries in python use {} key value pair {"key":"value"}
{
    "name": "John",
    "age": 30
}
{
    "lat": 0.00,
    "lng": 0.00
}
print(type({"name": "John", "age": 30}))  # dictionary


# range in python
range = 9
print(type(range))  # range

# set in python
print(type({1, 2, 3, 4, 5}))  # set

# frozenset in python
fronzenSet = frozenset({1, 2, 3, 4, 5})
print(type(fronzenSet))  # frozenset

# bytes in python
byteData = b"Hello"
print(type(byteData))  # bytes
