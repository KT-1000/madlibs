from random import choice, randint, sample

from flask import Flask, render_template, request, redirect


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

COOLPEEPS = sorted(['Meggie', 'Henry', 'Meg', 'Ally', 'Katie', 'Leslie', 'Joel',
                    'Veronica', 'Melissa', 'Inas', 'Anna', 'Allison', 'Julie',
                    'Aisling', 'Sarah', 'Nija', 'Kelsey', 'Katie', 'Monique',
                    'Patricia', 'Diana', 'Akyya', 'Aiden', 'Cristina', 'Emily',
                    'Kelly', 'Joyce', 'Katie', 'Maggie'])

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")
    print player

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_game_form():
    response = request.args.get("game")
    if response == "yes":
        return render_template("game.html", 
            people=COOLPEEPS,
            colors=COLORS)
    elif response == "no":
        return render_template("goodbye.html")
    else:
        return redirect("/hello")

@app.route('/madlib', methods=["GET","POST"])
def show_madlib():
    if request.method == "POST":
        person = request.form.get("person")

        color = request.form.getlist("color")
        color = "-".join(color)

        noun = request.form.get("noun")

        adjective = request.form.get("adjective")

        num = randint(1,4)

        return render_template("madlib.html",
                                num=num,
                                person=person,
                                color=color,
                                noun=noun,
                                adjective=adjective)

    elif request.method == "GET":
        return redirect('/hello')


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
