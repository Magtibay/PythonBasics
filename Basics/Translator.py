def translator(phrase):
    #Translate any vowel into the letter m
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOU".lower():
                if letter.isupper():
                    translation = translation + "M"
                else:
                    translation = translation + "m"
        else:
            translation = translation + letter          
    return translation

print(translator(input("Enter any phrase: ")))

repeat = input("Enter 'y' or 'yes to continue. Enter any other key to exit.").lower()


while repeat == "y" or  repeat== "yes":
    print(translator(input("Enter any phrase1: ").lower()))    
    repeat = input("Enter 'y' or 'yes to continue. Enter any other key to exit.").lower()
print("Goodbye.")

    


