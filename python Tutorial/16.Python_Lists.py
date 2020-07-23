# Python Collections (Arrays)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
print(len(thislist))

thislist[1] = "blackcurrant"
print(thislist)

thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist.remove("banana")
print(thislist)

thislist.pop()
print(thislist)

del thislist
print(thislist)


del thislist[0]
print(thislist)



thislist.clear()
print(thislist)

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

for x in thislist:
  print(x)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


for x in list2:
  list1.append(x)
print(list1)


list1.extend(list2)
print(list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# List Methods (built-in methods)
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

