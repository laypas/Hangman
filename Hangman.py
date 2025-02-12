""" 
#Laborationsinlämning: 23 feb 2025
#Projekt 1: Hangman

1. Skapa en version av det klassiska spelet Hangman.

    Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.
    Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.
    Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.
    Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.

2. Minst 3 commits i Git historik och två olika bransches. All kod och annan dokumentation skall finnas i repository.

    Inlämning av projektet:
        Skapa ett nytt repository på GitHub för ditt projekt. 
        Lägg till en README-fil med instruktioner för hur man använder programmet eller spelar spelet.
        Lägg till en .gitignore-fil för att exkludera onödiga filer från versionhantering. 
        Förslagsvis innehållande namnet på ditt virtual environement exempelvis (heter det venv har du venv/ på en rad i .gitignore)
        Pusha alla filer till ditt repository på GitHub.
        Lämna in en länk till ditt repository.
"""

import random 

def select_word():
    wordstr = "Fluffy,Cuddly,Ferrets,Lizard,Hamster,Penguin,Coyote,Parrots,Raccoon,Weasels,Stallion,Whiskers,Tailbone,Hooves,Antlers,Paws,Snout,Claws, Muzzle,Furball,Feather,Tentacle,Tusk,Horn,Scales,Zebra,Tiger,Lion,Bear,Deer"
    wordslist = [word.strip().upper() for word in wordstr.split(",")]

    random_word = random.choice(wordslist) #random word selection from worldlist
    return(random_word)


def host_respons(word, char): # word = list of chars, char = players guess as a char
    desplay_string = []
    for i in range(0, len(word)):
        if word[i] == char:
            desplay_string.append(char)
        else:
            desplay_string.append("_ ") 
    return(desplay_string)


def merge_lists(list1, list2):
    list3 = []
    for i in range(len(list1)): 
            if list1[i] != '_ ':
                list3.append(list1[i])
            elif list2[i] != '_ ':
                list3.append(list2[i])
            else:
                list3.append('_ ')
    return(list3)


def num_of_char_matches(list1, list2):
    s = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            s = s + 1
        else:
            s = s + 0 
    num_of_matches = s
    return(num_of_matches)


def player_won(list):
    for char in list:
        if char == '_ ':
            return(False)
    return(True)


def main():
    # Select Hangman word
    print("------randomly selected word--------")
    word = select_word()
    print(word)

    print("------test of list of chars in word and len of word--------")
    wordchars = list(word)
    print(wordchars)


    # User input, player starts guessing
    display_word  = host_respons(word, "")
    print("-----desplay_word----------------------------------------") 
    print(f"The word is? : {display_word}")

    players_guesses = []
    num_left = 8
    num = 0

    while num_left > 0:
        num = num + 1
        print("-----player guess------------------------------------------") 
        item = input(f"Your guesse no {num}. Please write a letter: ")
        players_guesses.append(item.upper())

        print("-----host responds with desplay string---------------------") 
        print(f"Your guesses: {players_guesses}")

        print("-----desplay of the word with correct guesses--------------") 
        saved_result = host_respons(word, item.upper())
        
        display_word = merge_lists(display_word, saved_result)
        print(display_word)

        print("-----num of guesses----------------------------------------") 
        num_correct = num_of_char_matches(players_guesses,display_word)
        num_wrong = len(players_guesses)-num_correct
        
        print("num correct guess:", num_correct)
        print("num wrong guess:", num_wrong)

        num_left = 8 - (len(players_guesses)-num_correct)
        print("num guesses left:", num_left)

        if player_won(display_word):
            break
    if num_left > 0:
        print(f"YOU WON THE GAME!!! YOU ARE AWSOME!!! 😍")
    else:
        print(f"YOU LOST THE GAME! THE END! 😵")
   
if __name__ == '__main__':
    main()