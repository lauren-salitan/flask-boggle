# from flask import Flask, request, render_template, redirect, session, flash, jsonify
# from boggle import Boggle

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
# boggle_game = Boggle()


# @app.route('/')
# def homepage():
#     """Show the board."""
#     board = boggle_game.make_board()
#     session['board'] = board
#     return render_template('board.html', board=board)


# @app.route('/check-word')
# def check_word():
#     """Check if word is in dictionary."""
#     word = request.args["word"]
#     board = session["board"]
#     response = boggle_game.check_valid_word(board, word)
#     return jsonify({'result': response})


# @app.route('/post-score', methods=["POST"])
# def post_score():
#     score = request.json["score"]
#     highscore = session.get("highscore", 0)
#     plays = session.get("plays", 0)
#     session["highscore"] = max(score, highscore)
#     session["plays"] = plays + 1
#     return jsonify(newRecord=score > highscore)

from flask import Flask, request, render_template, redirect, session, flash, jsonify
from flask_session import Session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

boggle_game = Boggle()

@app.route('/')
def homepage():
    """Show the board."""
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('board.html', board=board)

@app.route('/check-word')
def check_word():
    """Check if word is in dictionary."""
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)
    return jsonify({'result': response})

@app.route('/post-score', methods=["POST"])
def post_score():
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)
    session["highscore"] = max(score, highscore)
    session["plays"] = plays + 1
    return jsonify(newRecord=score > highscore)
