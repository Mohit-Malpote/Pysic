def translate(phrase):
    translation =""
    for word in phrase:
        if word.lower() in "manu,mrunali,you":
           translation=translation+"bokad"+phrase
        
    return translation
print(translate(input("What People say about u? :")))

#Complet from chat gpt 