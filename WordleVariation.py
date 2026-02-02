import random

#This is the method that tells user whether to go more towards end or beginning of alphabet.
#This was designed because a huge difficulty for the game was at the end finding the last letter
def alpha(guess, key):
    if guess < key:
        return "Try a word that is more towards the end of the alphabet"
    elif guess > key:
        return "Try a word that is more towards the beginning of the alphabet"
    else:
        return "You won!!!!!!!"
#This is a hint to reveal two letters, 
#Reveals one letter after 4th guess
#Reveals second letter after 5th guess
def reveal_letter(key, guess, reveal):
    possibilities = [i for i in range(len(key)) if guess[i] != key[i] and not reveal[i]]
    if not possibilities:
        possibilities = [i for i in range(len(key)) if not reveal[i]]
    if not possibilities:
        return None
    i = random.choice(possibilities)
    reveal[i] = True
    return i
#This is to actually print the guess
def hintp_rint(key, reveal):
    return "".join(key[i] if reveal[i] else "_" for i in range(len(key)))

#his is to load the database of words. 
#I have recieved these from an online database when I searched up "possible wordle guesses"
#Has around 13,000 words. Only 2000 are functional answers. 
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

#Whether the guess is actually valid or not
def possible(guess, guesses):
    return guess in guesses

#Tells whether the letter is green, yellow, or white

def grade(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i] + "\033[0m"
        elif guess[i] in word:
            str += "\033[33m" + guess[i] + "\033[0m"
        else:
            str += guess[i]

    return str + "\033[0m"
#Welcome message
#This is where the actual game takes place
def wordle(guesses, answers):
    print ("Welcome to Easy Mode of Wordle!")
    key = random.choice(answers)
    reveal = [False] * len(key)

    attempts = 1
    max_attempts = 6
#This is to prevent invalid guesses 
#No too many letters etc
    while attempts <= max_attempts:
        guess = input("Enter Guess " + str(attempts) + ": " ).lower()
        if not possible(guess, guesses):
            print("Guess a valid guess")
            continue
        if guess == key:
            print("You won")
            break
##Attempts will increase one by one
        attempts += 1
        feedback = grade(guess, key)
        
        print(feedback)
        
        print(alpha(guess, key))
    ##The Hint and the max attempts so game is not infinite. 
        if attempts > max_attempts:
                print("You lost. The Secret words was: " + key)
        if 4<= attempts <= 5:
            reveal_letter(key, guess, reveal)
            print("Your Hint is that a letter is: ", hintp_rint(key,reveal))

guesses = load_dictionary("allowed.txt")
answers = load_dictionary("allowed.txt")

wordle(guesses, answers)

