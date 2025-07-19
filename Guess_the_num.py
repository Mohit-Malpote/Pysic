import random

secret_num=random.randint(1,100)
attempts = 0
print("Thing a number between 1 to 100.")

attemps=0
while True:
    guess=int(input("Enter ypur guess :"))
    attemps += 1

    if guess == secret_num and attemps < 3:
        print("You win and with an exceptional performence with only "+ str(attemps)+" attemps")
        break
    elif guess == secret_num and attemps > 3:
        print("You win with "+str(attemps)+" attemps")
        break