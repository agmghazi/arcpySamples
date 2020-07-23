a = "Hello"
print(a)

ab = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(ab)


ac = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(ac)


ar = "Hello, World!"
print(ar[1])

b = "Hello, World!"
print(b[2:5])


bn = "Hello, World!"
print(bn[-5:-2])

an = "Hello, World!"
print(len(an))

aa = " Hello, World! "
print(aa.strip()) # returns "Hello, World!"

al = "Hello, World!"
print(al.lower())

au = "Hello, World!"
print(au.upper())

ap = "Hello, World!"
print(ap.replace("H", "J"))

at = "Hello, World!"
print(at.split(",")) # returns ['Hello', ' World!']


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print txt