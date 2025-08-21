#Hangman in Python
import random
from words_game import words 
###words=("apple","orange", "banana","coconut","pineapple")

#dictionary of key:()
hangman_art={0: ("     ",
                 "     ",
                 "     "),
             1: ("  O  ",
                 "     ",
                 "     "),
             2: ("  O  ",
                 "  |  ",
                 "     "),
             3: ("  O  ",
                 " /|  ",
                 "     "),
             4: ("  O  ",
                 " /|\\ ",
                 "     "),
             5: ("  O  ",
                 " /|\\ ",
                 " /  "),
             6: ("  O  ",
                 " /|\\ ",
                 " / \\ ")}


def display_man(guesses_wrong):
    print("******************************")
    for line in hangman_art[guesses_wrong]:
        print(line)
    print("******************************")

def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"] * len(answer)
    ##print(hint)
    guesses_wrong=0
    guessed_wrong=[]
    guessed_letters=set()
    is_running=True

    while is_running:
        display_man(guesses_wrong)
        display_hint(hint)
        ###display_answer(answer)
        guess=input("Enter a letter: ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("invalid input!")
            continue
            ###continue pt a da skip la ce i de desupt si trece la urmatorea 
            ### iteratie de la loop adica in cazul nostru la while inapoi

        if guess in guessed_letters:
            print(f"letter {guess} is already guessed")
            continue

        guessed_letters.add(guess)
    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                   hint[i] = guess 
        else:
            guesses_wrong+=1
            guessed_wrong.append(guess)
            print(f"{guesses_wrong} letters guessed wrong: ")
            print(guessed_wrong)

            

        if "_" not in hint:
            display_man(guesses_wrong)
            display_answer(answer)
            print("you win")
            is_running=False
        elif guesses_wrong >= len(hangman_art)- 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU")
                
                
if __name__=="__main__":
    main()
