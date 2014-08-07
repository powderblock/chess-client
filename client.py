#This must be run in an interactive shell.
import chess
from chessboard import *

game = chess.Game()
chess.debug(True)
player = game.join()
gameinput = raw_input("Enter a game_id to join a game:\n")
game = chess.Game(game_id=gameinput)
draw()
