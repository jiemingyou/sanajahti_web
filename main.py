from flask import Flask, redirect, url_for, render_template, request
from sanajahti import Game
import time

app = Flask(__name__)

def get_letters():
    # Collection user input
    input = []
    for row in range(1,5):
        for col in range(1,5):
            input.append(request.form[f"r{row}c{col}"])
    
    return input


# Landing page
@app.route("/", methods=["POST", "GET"])
def landing():

    if request.method == "POST":
        letters = get_letters()
        
    # ----
        words = set()
        with open("kotus_wordlist.txt") as f:
            for word in f:
                word = word.strip()
                words.add(word)
                
        ans = Game(letters, words).solve()
    # ----

        print(letters, ans)
        return render_template("solve.html", answer="\n".join(ans))

    else:
        return render_template("solve.html", answer="")


if __name__ == "__main__":
    app.run()