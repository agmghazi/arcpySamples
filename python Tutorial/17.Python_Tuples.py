
# Note:Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# Note: You cannot remove items in a tuple.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Tuple     Methods
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
