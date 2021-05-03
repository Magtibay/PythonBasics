secret_word = "hyperlink"
guess_tries = 3
guess_limit = 0
game_lost = False

print("You have" , guess_tries , "tries to guess the secret word correctly!")

guess = input("Please enter your guess of the secret word: ").lower()
guess_tries -= 1

while guess != secret_word and not (game_lost):
    if guess_tries > guess_limit:
        print("INCORRECT!\nyou have:" , guess_tries , "tries left!")
        guess = input("Enter your guess word: ").lower()
        guess_tries -= 1      
    else:
        game_lost = True
        
if game_lost:  
    print("You Lose")
else:
    print("CORRECT! YOU WIN!")

    