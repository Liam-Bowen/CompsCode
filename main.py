import math

import team

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    team.team()
# def hello():
# return 'Hello World'

# export FLASK_APP=hello
# export FLASK_ENV=development
# flask run


main()
