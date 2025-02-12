# Hangman App
from flask import Flask, redirect, render_template, request
from flask import send_from_directory
from Hangman import select_word, host_respons,merge_lists, num_of_char_matches, player_won

app = Flask(__name__)

def reset_game_word():
    global word
    global display_word
    global players_guesses

    word = list(select_word())
    display_word = host_respons(word, "")
    players_guesses = []

reset_game_word()

@app.route("/", methods=["POST", "GET"])
def home():
    global display_word
    global players_guesses

    print("selected word:")
    print(word)

    print("players guess:")
    print(request.form)
    print(players_guesses)

    print("display word: before guess:")
    print(display_word)

    if request.form:
        for c in request.form:
            players_guesses.append(c)
            saved_result = host_respons(word, c.upper())

            print("display word: after guess:")
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
    return send_from_directory("images", path)

@app.route("/reset", methods=["GET"])
def resetgame():
    reset_game_word()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

 