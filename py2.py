# ---Tuples---

# coordinates = (4,5)  #we can also make lists of tuples 
# # coordinates[1] = 10    the contents in the tuples cannot change 
#  print(coordinates[0])

# ---Funtions---

def say_hi(name, age): # def funName()
    print("Hello "+name + ", you are "+ str(age) )

print("top")
say_hi("Mohit", 18)
say_hi("Sahil", 21)
print("BOTTOM")

# ---Return Statement---

def cube(num):
    import math
    return math.pow(num,3) # it returns the value from function , 
                           #also this is the last line of the function

print(cube(4))

# ---If Statements---

is_male = True
is_tall = True

if is_male and is_tall :   #we can also use or oprator at the place of and 
    print("You are a tall male")
elif is_male and not(is_tall): #elif= else-if, not()is nigetion
    print("YOUARE A SHORT MALE")
elif is_tall and not(is_male):
    print("You are tall but not male")
else :
    print("You are not male nor tall")

# ---If Statement&Comparision---

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3 :
        return num1 
    elif num2>=num1 and num2>=num3:
        return num2
    else :
        return num3
print(max_num(3,30,5))