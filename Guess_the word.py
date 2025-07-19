print("This is a Synonym of the word 'lie'")

Secret_word = "untrue"
guess=""
guess_count =0
guess_limit = 3
Out_of_guess =False

while guess != Secret_word and Out_of_guess==False:
    
    if guess_count<guess_limit:
       guess= input("Enter the word :")
       guess_count += 1
    else:
        Out_of_guess= True

if Out_of_guess:
    print("Out of guess, You lose")
else:
    print("you win")

