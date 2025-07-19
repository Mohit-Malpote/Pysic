P = float(input("Investment amount per month :"))
R = float(input("Annual intrest rate :"))
T = float(input("Period of investment :"))

r = R/12/100
n = T*12

FV = P * (((1 + r)**n - 1) / r) * (1 + r)

print("Amount invested is "+ str(P*n))
print("Final amount is "+ str(FV))
print("Wealth gained "+ str(FV-(P*n)))