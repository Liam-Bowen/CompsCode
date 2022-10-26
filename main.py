from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def my_team():
    return render_template('home.html')


@app.route('/standings')
def standings():
    return render_template('standings.html')


@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')


@app.route('/add-players')
def add_players():
    return render_template('add_players.html')


@app.route('/draft-room')
def draft_room():
    return render_template('draft_room.html')


@app.route('/my-team')
def my_team2():
    return render_template('my_team.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/test2')
def test2():
    return render_template('test2.html')


app.run(debug=True)

