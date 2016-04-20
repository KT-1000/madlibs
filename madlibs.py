from random import choice, randint

from flask import Flask, render_template, request


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

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    response = request.args.get("game")
    if response == "yes":
        return render_template("game.html", 
            people=COOLPEEPS,
            colors=COLORS)
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")

    color = request.args.getlist("color")
    color = "-".join(color)

    noun = request.args.get("noun")

    adjective = request.args.get("adjective")

    num = randint(1,4)

    return render_template("madlib.html",
                            num=num,
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
