thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


x = thisdict["model"]
print x


x = thisdict.get("model")
print x


thisdict["year"] = 2018
print thisdict


for x in thisdict:
  print(x)
  print(thisdict[x])


for x in thisdict.values():
  print(x)


for x, y in thisdict.items():
  print(x, y)


if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


print(len(thisdict))



thisdict["color"] = "red"
print(thisdict)


thisdict.pop("model")
print(thisdict)


thisdict.popitem()
print(thisdict)


del thisdict["model"]
print(thisdict)


thisdict.clear()
print(thisdict)


mydict = thisdict.copy()
print(mydict)


mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print myfamily


thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


# Dictionary Methods
# Method    	Description
# clear()	    Removes all the elements from the dictionary
# copy()     	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()   	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()   	Updates the dictionary with the specified key-value pairs
# values()    	Returns a list of all the values in the dictionary


# https://www.w3schools.com/python/python_dictionaries.asp