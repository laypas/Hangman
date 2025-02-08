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
    wordstr = "Fluffy, Cuddly, Ferrets, Bearded, Lizard, Hamster, Penguin, Coyote, Parrots, Raccoon, Weasels, Stallion, Whiskers,Tailbone, Hooves, Antlers, Paws, Snout, Claws, Muzzle, Furball,Feather, Tentacle, Tusk, Horn, Scales"
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
    #list1 = ['F', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
    # = ['_', 'E ', '_ ', '_ ', '_ ', '_ ', '_ ']
    list3 = []

    for i in range(len(list1)): 
            if list1[i] != '_ ':
                list3.append(list1[i])
            elif list2[i] != '_ ':
                list3.append(list2[i])
            else:
                list3.append('_ ')
    return(list3)


def main():
    # Select hangman word
    print("------randomly selected word--------")
    word = select_word()
    print(word)

    print("------test of list of chars in word and len of word--------")
    wordchars = list(word)
    print(wordchars)

    print(len(wordchars)) #prints the last element in the list (index = 7)
    #print(wordchars[-1]) #prints the last letter in the list (value = "R")


    # User input, player starts guessing

    desplay_word  = host_respons(word, "")
    print("-----desplay_word---------------------") 
    print(f"The word is? : {desplay_word}")


    players_guesses = []
    for i in range(8):  # max 8 guesses
        num = i +1

        print("-----player guess---------------------") 
        item = input(f"Your guesse no {num}. Please write a letter: ")
        players_guesses.append(item.upper())

        print("-----host responds with desplay string---------------------") 
        print(f"Your geusses: {players_guesses}")
        print(players_guesses[i])

        print("-----desplay of the word with correct guesses---------------------") 
        saved_result = host_respons(word, item.upper())
        #print(saved_result)
        
        desplay_word = merge_lists(desplay_word, saved_result)
        print(desplay_word)

main()
