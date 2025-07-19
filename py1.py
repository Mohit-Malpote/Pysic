print("Hello World")

# ---Variables---

char_name="Sam"
char_age="46"
print("there was a men named " + char_name+" , ")
print("he was " +char_age+ " years old. ")

char_name = "Mike"
print("He really liked the name "+ char_name+" , ")
print("but didn't like being "+char_age+" .")

# ---String---

phrase = "Mahatma School"
print (phrase.upper().isupper())

# Function	Meaning / Use
# upper()	Converts all characters to uppercase.
# lower()	Converts all characters to lowercase.
# capitalize()	Capitalizes first letter of the string.
# title()	Capitalizes first letter of every word.
# swapcase()	Swaps case of all characters (upper ⇄ lower).
# strip()	Removes spaces from both ends of the string.
# lstrip()	Removes spaces from the left side.
# rstrip()	Removes spaces from the right side.
# find(sub)	Returns the index of first occurrence of sub, or -1 if not found.
# index(sub)	Same as find() but raises an error if not found.
# replace(old, new)	Replaces old substring with new.
# startswith(sub)	Returns True if string starts with sub.
# endswith(sub)	Returns True if string ends with sub.
# split(delim)	Splits string into list based on delimiter (default is space).
# join(list)	Joins elements of a list into one string.
# count(sub)	Counts how many times sub appears.
# isalpha()	Returns True if all characters are alphabets.
# isdigit()	Returns True if all characters are digits.
# isalnum()	Returns True if all characters are letters or digits.
# isupper()	Returns True if all characters are uppercase.
# islower()	Returns True if all characters are lowercase.

# ---Working With Numbers---
import math #this brings many functions for numbers 

my_num= 5
print(math.sqrt(my_num))

# Function	Meaning / Use	Example
# abs(x)	Returns absolute value of x	abs(-5) → 5
# round(x, n)	Rounds x to n decimal places	round(3.14159, 2) → 3.14
# pow(x, y)	Returns x raised to the power y	pow(2, 3) → 8
# divmod(x, y)	Returns a tuple (x // y, x % y) (quotient, remainder)	divmod(10, 3) → (3, 1)
# max(a, b, ...)	Returns the maximum value	max(3, 7, 1) → 7
# min(a, b, ...)	Returns the minimum value	min(3, 7, 1) → 1
# sum(iterable)	Returns the sum of all elements in a list	sum([1, 2, 3]) → 6
# int(x)	Converts a float or string to an integer	int(3.9) → 3
# float(x)	Converts an integer or string to float	float(5) → 5.0
# math.sqrt(x)	Square root of x	math.sqrt(9) → 3.0
# math.pow(x, y)	x raised to the power y	math.pow(2, 3) → 8.0
# math.floor(x)	Rounds x down to nearest integer	math.floor(3.9) → 3
# math.ceil(x)	Rounds x up to nearest integer	math.ceil(3.1) → 4
# math.factorial(x)	Returns factorial of x	math.factorial(5) → 120
# math.log(x)	Natural log (base e) of x	math.log(10) → 2.302...
# math.log10(x)	Base-10 log of x	math.log10(100) → 2.0
# math.sin(x)	Sine of x (x in radians)	math.sin(math.pi/2) → 1.0
# math.cos(x)	Cosine of x	math.cos(0) → 1.0
# math.tan(x)	Tangent of x	math.tan(1) → 1.557...
# math.gcd(a, b)	Greatest common divisor of a and b	math.gcd(12, 8) → 4
# math.lcm(a, b)	Least common multiple	math.lcm(4, 6) → 12
# math.isqrt(x)	Integer square root (no decimals)	math.isqrt(10) → 3
# math.degrees(x)	Converts radians to degrees	math.degrees(math.pi) → 180
# math.radians(x)	Converts degrees to radians	math.radians(180) → π
# math.pi	Returns constant π	math.pi → 3.14159...
# math.e	Returns constant e	math.e → 2.71828...

# ---Input---

num_1=float(input("Enter first number:"))
num_2=float(input("Enter second number:"))
print(num_1+num_2)

# ---List---

lucky_number = [3,45,66,42,56, "two"]
friends= ["mohit","rohit","ram"]
friends.extend(lucky_number)
print(friends)

# append(x)	Adds item x at the end of the list	my_list.append(2) → [3, 1, 4, 1, 5, 9, 2]
# insert(i, x)	Inserts x at index i	my_list.insert(2, 7) → [3, 1, 7, 4, 1, 5, 9]
# extend(list2)	Adds all items from list2 to the end	my_list.extend([6,7]) → [3,1,4,1,5,9,6,7]
# remove(x)	Removes first occurrence of x	my_list.remove(1) → [3, 4, 1, 5, 9]
# pop()	Removes and returns the last item	my_list.pop() → returns 9, list is now [3, 1, 4, 1, 5]
# pop(i)	Removes and returns the item at index i	my_list.pop(2) → returns 4
# clear()	Removes all items from the list	my_list.clear() → []
# index(x)	Returns index of first occurrence of x	my_list.index(5) → 4
# count(x)	Returns how many times x occurs	my_list.count(1) → 2
# sort()	Sorts list in ascending order (modifies original)	my_list.sort() → [1, 1, 3, 4, 5, 9]
# sort(reverse=True)	Sorts list in descending order	my_list.sort(reverse=True) → [9, 5, 4, 3, 1, 1]
# reverse()	Reverses the order of elements	my_list.reverse() → reversed list
# copy()	Returns a shallow copy of the list	copy_list = my_list.copy()
# len(list)	Returns the number of items	len(my_list) → 6
# sum(list)	Returns the sum of all items	sum(my_list) → 23
# max(list)	Returns the largest item	max(my_list) → 9
# min(list)	Returns the smallest item	min(my_list) → 1
# list()	Converts a tuple/string to a list	list("abc") → ['a', 'b', 'c']


