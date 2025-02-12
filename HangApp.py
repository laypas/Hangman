# Hangman App
from flask import Flask, redirect, render_template, request
from flask import send_from_directory
from Hangman import select_word, host_respons,merge_lists, num_of_char_matches, player_won

app = Flask(__name__)

word = list(select_word())
players_guesses = []
display_word = host_respons(word, "")

@app.route("/", methods=["POST", "GET"])
def home():
    global display_word
    print(request.form)
    print(word)
    print(players_guesses)
    print(display_word)

    if request.form:
        for c in request.form:
            players_guesses.append(c)
            print(players_guesses)

            saved_result = host_respons(word, c.upper())
            print(saved_result)

            display_word = (merge_lists(display_word, saved_result))
            print(display_word)


    num_correct = num_of_char_matches(players_guesses,display_word)
    num_wrong   = len(players_guesses) - num_correct
    num_left    = 8 -(len(players_guesses) - num_correct)

    return render_template("HangTemp.html"
                           , word=display_word
                           , players_guesses=players_guesses
                           , num_correct=num_correct
                           , num_wrong=num_wrong
                           , num_left=num_left
                           , player_won=player_won(display_word)
                           , player_lost=num_left<=0
                           )

@app.route("/images/<path:path>")
def send_report(path):
    return send_from_directory("C:\\Images", path)

@app.route("/reset", methods=["GET"])
def resetgame():
    global players_guesses
    players_guesses = []

    global display_word
    display_word = host_respons(word, "")
    return redirect("/")

 
if __name__ == "__main__":
    app.run(debug=True)

 