def translate(phrase):
    translation =""
    #split the sentance into words
    words = phrase.split()
    for word in words:
        if word.lower() in ["mohit"]:
           if word.isupper:
               translation+="Aryan"
           else:
               translation+=" aryan "
           
        else:
            translation += word + " "
        
    return translation
print(translate(input("What People say about u? :")))

