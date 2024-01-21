from flask import Flask, render_template, request, redirect
import random

# intializing an app
app = Flask(__name__)
count = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        global x
        x = random.randint(start, end)
        return redirect("/guess")
    else:
        return render_template("range.html")


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    global x, count
    print("x @index_function is: ", x)
    message = "Start The Guess !!"
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        if user_guess == x:
            message = "You Guessed Right !!!"
            return render_template("guess.html", message=message, count=count)
        elif user_guess < x:
            message = " Too Small Guess"
            count += 1
            return render_template("guess.html", message=message, count=count)
        else:
            message = "Too High Buddy !!!"
            count += 1
            return render_template("guess.html", message=message, count=count)
    else:
        return render_template("guess.html", message=message, count=count)


if __name__ == "__main__":
    app.run(debug=True)
