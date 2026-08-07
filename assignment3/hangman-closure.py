#Task 4
def make_hangman(secret_word):
    guesses = [ ]
    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""
        for letter in secret_word:
            if letter in guesses:
                display_word += letter
            else:
                display_word += "_"
        print (display_word)
        if all(letter in guesses for letter in secret_word):
            return True
        else:
            return False
    return hangman_closure
secret_word = input("Enter the secret word: ")
hangman_game = make_hangman(secret_word)
while True:
    players_guess = input("Try and guess a letter:")
    if hangman_game(players_guess):
        print ("Yaaay! You guessed the word! :)")
        break