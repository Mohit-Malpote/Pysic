# ---Dictionaries---

NumToMonth = {
    1:"January",
    2: "February",
    3: "March",
    4: "April",
    5:"May",
    6:"June"
}
print(NumToMonth[4])
print(NumToMonth.get(3))
print(NumToMonth.get("man","Unvalid keyword")) 
#we can give a defult value on non listed terms 
print(NumToMonth.get("man"))

# ---While loop---
i=1
while i<=10:
    print(i)
    i +=1  #increment by 1
print("done with the loop")

# ---For Loop---
friends = ["jim","Karen","Kevin"] 
# it is use to loop through any collections like array

for friend in friends :
    print(friend)

for index in range(5): 
#can also write if statement or any othe complex with it
    if index ==0:
        print("first iteration")
    else:
        print("not first")
    # print(index)

# ---Exponent function---

def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result=result*base_num
    return result

# print(raise_to_power(2,3))
base =int(input("Enter the base number:"))
pow =int(input("Enter the power: "))
print(raise_to_power(base,pow))