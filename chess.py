# chess.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from board import Board
from tkinter import *
from chessGUI import chessGUI
import argparse         # used to process comand line inputs
import sys              # used to print error messages
import copy


inputA = [['_', '_', '_', '_', '_', '_', 'q', 'k'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', 'P', '_', 'p'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', 'Q', 'P'],
['_', '_', '_', '_', '_', 'P', 'P', '_'],
['_', '_', '_', '_', 'R', '_', 'K', '_']]

inputB = [['_', '_', 'B', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', 'K', '_', '_', '_', '_'],
['_', 'p', '_', '_', '_', '_', '_', '_'],
['_', '_', 'k', '_', '_', '_', '_', '_'],
['P', '_', '_', '_', '_', 'P', '_', '_'],
['_', 'B', '_', '_', '_', '_', '_', '_'],
['N', '_', '_', '_', '_', 'N', '_', '_']]

inputC = [['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', 'K', '_', '_', '_', '_'],
['_', '_', 'R', '_', 'P', '_', '_', '_'],
['_', 'P', '_', 'k', 'r', '_', '_', '_'],
['_', '_', '_', 'N', 'p', 'b', '_', '_'],
['_', '_', '_', '_', 'P', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', 'N', '_', '_']]

inputFull = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

inputTest1 = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'N', 'p', 'p', 'p', '_', 'p'],
['P', '_', '_', 'P', '_', '_', 'R', '_'],
['_', '_', 'Q', 'B', 'N', '_', 'p', '_'],
['_', '_', '_', '_', 'K', '_', '_', 'P'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', 'P', 'P', '_', 'P', 'P', 'P', '_'],
['R', '_', 'B', '_', '_', '_', '_', '_']]

inputTest2 = [['_', '_', '_', '_', 'k', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', 'K', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_']]





###############################################################################
#                                    GLOBAL                                   #
###############################################################################

# command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('Arguments', metavar='N', type=int, nargs='+')
arguments = parser.parse_args()

# error messages
if(len(arguments.Arguments) != 1):
    sys.exit("    Error: Incorrect number of command line arguments supplied; 1 needed")

usedBoard = arguments.Arguments[0]             # which given puzzle to solve


# determine which of the initial boards we are using
inputGrid = None
if(usedBoard == 1):
    inputGrid = inputA
elif(usedBoard == 2):
    inputGrid = inputB
elif(usedBoard == 3):
    inputGrid = inputC
elif(usedBoard == 4):
    inputGrid = inputFull
elif(usedBoard == 5):
    inputGrid = inputTest1
elif(usedBoard == 6):
    inputGrid = inputTest2



boardDefault = Board(inputGrid, True)           # create initial Board object
boardDefault.printBoard()                       # print to terminal the Board (text)
#graphicalBoard(boardDefault)                    # launch graphical window of the Board
chessGUI(boardDefault)






