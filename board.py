###############################################################################
#
# 
#
###############################################################################  
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from tkinter import *
import copy

###############################################################################
#
# 
#
###############################################################################  
class Board():

    
    pEval = [[0, 0, 0, 0, 0, 0, 0, 0],
                [50, 50, 50, 50, 50, 50, 50, 50],
                [10, 10, 20, 30, 30, 20, 10, 10],
                [5, 5, 10, 25, 25, 10, 5, 5],
                [0, 0, 0, 20, 20, 0, 0, 0],
                [5, -5, -10, 0, 0, -10, -5, 5],
                [5, 10, 10, -20, -20, 10, 10, 5],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    PEval = [[0, 0, 0, 0, 0, 0, 0, 0],
                [5, 10, 10, -20, -20, 10, 10, 5],
                [5, -5, -10, 0, 0, -10, -5, 5],
                [0, 0, 0, 20, 20, 0, 0, 0],
                [5, 5, 10, 25, 25, 10, 5, 5],
                [10, 10, 20, 30, 30, 20, 10, 10],
                [50, 50, 50, 50, 50, 50, 50, 50],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    nEval = [[-50, -40, -30, -30, -30, -30, -40, -50],
                    [-40, -20, 0, 0, 0, 0, -20, -40],
                    [-30, 0, 10, 15, 15, 10, 0, -30],
                    [-30, 5, 15, 20, 20, 15, 5, -30],
                    [-30, 0, 15, 20, 20, 15, 0, -30],
                    [-30, 5, 10, 15, 15, 10, 5, -30],
                    [-40, -20, 0, 5, 5, 0, -20, -40],
                    [-50, -40, -30, -30, -30, -30, -40, -50]]

    NEval = [[-50, -40, -30, -30, -30, -30, -40, -50],
                    [-40, -20, 0, 5, 5, 0, -20, -40],
                    [-30, 5, 10, 15, 15, 10, 5, -30],
                    [-30, 0, 15, 20, 20, 15, 0, -30],
                    [-30, 5, 15, 20, 20, 15, 5, -30],
                    [-30, 0, 10, 15, 15, 10, 0, -30],
                    [-40, -20, 0, 0, 0, 0, -20, -40],
                    [-50, -40, -30, -30, -30, -30, -40, -50]]

    bEval = [[-20, -10, -10, -10, -10, -10, -10, -20],
                    [-10, 0, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 5, 10, 10, 5, 0, -10],
                    [-10, 5, 5, 10, 10, 5, 5, -10],
                    [-10, 0, 10, 10, 10, 10, 0, -10],
                    [-10, 10, 10, 10, 10, 10, 10, -10],
                    [-10, 5, 0, 0, 0, 0, 5, -10],
                    [-20, -10, -10, -10, -10, -10, -10, -20]]

    BEval = [[-20, -10, -10, -10, -10, -10, -10, -20],
                    [-10, 5, 0, 0, 0, 0, 5, -10],
                    [-10, 10, 10, 10, 10, 10, 10, -10],
                    [-10, 0, 10, 10, 10, 10, 0, -10],
                    [-10, 5, 5, 10, 10, 5, 5, -10],
                    [-10, 0, 5, 10, 10, 5, 0, -10],
                    [-10, 0, 0, 0, 0, 0, 0, -10],
                    [-20, -10, -10, -10, -10, -10, -10, -20]]

    rEval = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [5, 10, 10, 10, 10, 10, 10, 5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [0, 0, 0, 5, 5, 0, 0, 0]]

    REval = [[0, 0, 0, 5, 5, 0, 0, 0],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [-5, 0, 0, 0, 0, 0, 0, -5],
                    [5, 10, 10, 10, 10, 10, 10, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

    qEval = [[-20, -10, -10, -5, -5, -10, -10, -20],
                    [-10, 0, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 5, 5, 5, 5, 0, -10],
                    [-5, 0, 5, 5, 5, 5, 0, -5],
                    [0, 0, 5, 5, 5, 5, 0, -5],
                    [-10, 5, 5, 5, 5, 5, 0, -10],
                    [-10, 0, 5, 0, 0, 0, 0, -10],
                    [-20, -10, -10, -5, -5, -10, -10, -20]]

    QEval = [[-20, -10, -10, -5, -5, -10, -10, -20],
                    [-10, 0, 5, 0, 0, 0, 0, -10],
                    [-10, 5, 5, 5, 5, 5, 0, -10],
                    [0, 0, 5, 5, 5, 5, 0, -5],
                    [-5, 0, 5, 5, 5, 5, 0, -5],
                    [-10, 0, 5, 5, 5, 5, 0, -10],
                    [-10, 0, 0, 0, 0, 0, 0, -10],
                    [-20, -10, -10, -5, -5, -10, -10, -20]]

    kEval = [[-30, -40, -40, -50, -50, -40, -40, -30],
                    [-30, -40, -40, -50, -50, -40, -40, -30],
                    [-30, -40, -40, -50, -50, -40, -40, -30],
                    [-30, -40, -40, -50, -50, -40, -40, -30],
                    [-20, -30, -30, -40, -40, -30, -30, -20],
                    [-10, -20, -20, -20, -20, -20, -20, -10],
                    [20, 20, 0, 0, 0, 0, 20, 20],
                    [20, 30, 10, 0, 0, 10, 30, 20]]

    KEval = [[20, 30, 10, 0, 0, 10, 30, 20],
                    [20, 20, 0, 0, 0, 0, 20, 20],
                    [-10, -20, -20, -20, -20, -20, -20, -10],
                    [-20, -30, -30, -40, -40, -30, -30, -20],
                    [-30, -40, -40, -50, -50, -40, -40, -30],
                    [-30, -40, -40, -50, -50, -40, -40, -30],
                    [-30, -40, -40, -50, -50, -40, -40, -30],
                    [-30, -40, -40, -50, -50, -40, -40, -30]]


    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def __init__(self, grid, newBoard = False, whiteInCheck = False, blackInCheck = False):
        
        if(newBoard == True):

            self.mobility = 0
            self.bMobility = 0
            self.grid = [[None for x in range(0,8)] for y in range(0,8)]
            for i in range(0,8):
                for j in range(0,8):
                    if(grid[i][j] == '_' or grid[i][j] == '-'):
                        self.grid[i][j] = None
                    elif(grid[i][j] == 'P'):
                        self.grid[i][j] = Pawn(i, j, 'w', 'P')
                    elif(grid[i][j] == 'p'):
                        self.grid[i][j] = Pawn(i, j, 'b', 'p')
                    elif(grid[i][j] == 'N'):
                        self.grid[i][j] = Knight(i, j, 'w', 'N')
                    elif(grid[i][j] == 'n'):
                        self.grid[i][j] = Knight(i, j, 'b', 'n')
                    elif(grid[i][j] == 'B'):
                        self.grid[i][j] = Bishop(i, j, 'w', 'B')
                    elif(grid[i][j] == 'b'):
                        self.grid[i][j] = Bishop(i, j, 'b', 'b')
                    elif(grid[i][j] == 'Q'):
                        self.grid[i][j] = Queen(i, j, 'w', 'Q')
                    elif(grid[i][j] == 'q'):
                        self.grid[i][j] = Queen(i, j, 'b', 'q')
                    elif(grid[i][j] == 'K'):
                        self.grid[i][j] = King(i, j, 'w', 'K')
                    elif(grid[i][j] == 'k'):
                        self.grid[i][j] = King(i, j, 'b', 'k')
                    elif(grid[i][j] == 'R'):
                        self.grid[i][j] = Rook(i, j, 'w', 'R')
                    elif(grid[i][j] == 'r'):
                        self.grid[i][j] = Rook(i, j, 'b', 'r')
            self.whiteInCheck = whiteInCheck  # change later maybe?
            self.blackInCheck = blackInCheck  # change later maybe?

        else:
            self.mobility = 0
            self.bMobility = 0
            self.grid = grid
            self.whiteInCheck = whiteInCheck  # change later maybe?
            self.blackInCheck = blackInCheck  # change later maybe?

        self.evalValue = self.evaluationFunction()

        # print("EvalValue:", self.evalValue)




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def evaluationFunction(self):
        whiteCount = 0
        blackCount = 0 

        for i in range(8):
            for j in range(8):
                if self.grid[i][j] != None:
                    if self.grid[i][j].color == 'w':
                        if self.grid[i][j].id == 'P':
                            whiteCount = whiteCount + 100
                            self.mobility = self.mobility + Board.pEval[i][j]
                        elif self.grid[i][j].id == 'N':
                            whiteCount = whiteCount + 320
                            self.mobility = self.mobility + Board.nEval[i][j]
                        elif self.grid[i][j].id == 'B':
                            whiteCount = whiteCount + 330
                            self.mobility = self.mobility + Board.bEval[i][j]
                        elif self.grid[i][j].id == 'Q':
                            whiteCount = whiteCount + 900
                            self.mobility = self.mobility + Board.qEval[i][j]
                        elif self.grid[i][j].id == 'R':
                            whiteCount = whiteCount + 500
                            self.mobility = self.mobility + Board.rEval[i][j]
                        elif self.grid[i][j].id == 'K':
                            whiteCount = whiteCount + 20000
                            self.mobility = self.mobility + Board.kEval[i][j]
                    if self.grid[i][j].color == 'b':
                        if self.grid[i][j].id == 'p':
                            blackCount = blackCount + 100
                            self.bMobility = self.bMobility + Board.rEval[i][j]
                        elif self.grid[i][j].id == 'n':
                            blackCount = blackCount + 320
                            self.bMobility = self.bMobility + Board.rEval[i][j]
                        elif self.grid[i][j].id == 'b':
                            blackCount = blackCount + 330
                            self.bMobility = self.bMobility + Board.rEval[i][j]
                        elif self.grid[i][j].id == 'q':
                            blackCount = blackCount + 900
                            self.bMobility = self.bMobility + Board.rEval[i][j]
                        elif self.grid[i][j].id == 'r':
                            blackCount = blackCount + 500
                            self.bMobility = self.bMobility + Board.rEval[i][j]
                        elif self.grid[i][j].id == 'k':
                            blackCount = blackCount + 20000
                            self.bMobility = self.bMobility + Board.rEval[i][j]

        if(self.isWhiteInCheckmate() ): 
            return(-100000)
        if(self.isBlackInCheckmate()):
            return(100000)

        self.mobility = 0.5*self.mobility
        self.bMobility = 0.5*self.bMobility

        #print("Eval: ", whiteCount - blackCount + self.mobility + self.bMobility)
        return(whiteCount - blackCount + self.mobility + self.bMobility)


    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def isWhiteInCheckmate(self):
        tempList = None
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None and self.grid[i][j].color == 'w'):
                    tempList = self.grid[i][j].move(self)
                    if(len(tempList) != 0):
                        return(False)
        return(True)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def isBlackInCheckmate(self):
        tempList = None
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None and self.grid[i][j].color == 'b'):
                    tempList = self.grid[i][j].move(self)
                    if(len(tempList) != 0):
                        return(False)
        return(True)




    # for all white pieces, find their valid moves by calling their move() function
    # then create a new board for each of those valid moves
    # return a list of these new boards
    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def generateAllWhiteMoves(self, strategy):
        boardList = []
        if(strategy == 1):
            for i in range(8):
                for j in range(8):
                    if(self.grid[i][j] != None):
                        if(self.grid[i][j].color == 'w'):  # all white pieces
                            
                            # coordinates where we are moving a particular piece
                            newMovesCoords = self.grid[i][j].move(self)    

                            # for each of those coordinate pairs, create new board
                            for x in newMovesCoords:
                                tempBoard = Board(copy.deepcopy(self.grid))
                                tempBoard.grid[x[0]][x[1]] = tempBoard.grid[i][j]
                                tempBoard.grid[x[0]][x[1]].i = x[0]         # do we need this elsewhere???
                                tempBoard.grid[x[0]][x[1]].j = x[1]
                                tempBoard.grid[i][j] = None
                                tempBoard.evalValue = tempBoard.evaluationFunction()
                                boardList.append(tempBoard)
                                
        if(strategy == 2):
            queenMoves = []
            bishopMoves = []
            rookMoves = []
            knightMoves = []
            kingMoves = []
            pawnMoves = []
            for i in range(8):
                for j in range(8):
                    if(self.grid[i][j] != None):
                        if(self.grid[i][j].color == 'w'):  # all white pieces
                            
                            # coordinates where we are moving a particular piece
                            newMovesCoords = self.grid[i][j].move(self)    

                            # for each of those coordinate pairs, create new board
                            for x in newMovesCoords:
                                tempBoard = Board(copy.deepcopy(self.grid))
                                tempBoard.grid[x[0]][x[1]] = tempBoard.grid[i][j]
                                tempBoard.grid[x[0]][x[1]].i = x[0]         # do we need this elsewhere???
                                tempBoard.grid[x[0]][x[1]].j = x[1]
                                tempBoard.grid[i][j] = None
                                tempBoard.evalValue = tempBoard.evaluationFunction()
                                if(self.grid[i][j].id == 'Q'):
                                    queenMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'B'):
                                    bishopMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'R'):
                                    rookMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'N'):
                                    knightMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'K'):
                                    kingMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'P'):
                                    pawnMoves.append(copy.deepcopy(tempBoard))
            for x in queenMoves:
                boardList.append(x)
            for x in bishopMoves:
                boardList.append(x)
            for x in rookMoves:
                boardList.append(x)
            for x in knightMoves:
                boardList.append(x)
            for x in kingMoves:
                boardList.append(x)
            for x in pawnMoves:
                boardList.append(x)

        return(boardList)

    
    # for all black pieces, find their valid moves by calling their move() function
    # then create a new board for each of those valid moves
    # return a list of these new boards
    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def generateAllBlackMoves(self, strategy):
        boardList = []
        if(strategy == 1):
            for i in range(8):
                for j in range(8):
                    if(self.grid[i][j] != None):
                        if(self.grid[i][j].color == 'b'):  # all white pieces
                            
                            # coordinates where we are moving a particular piece
                            newMovesCoords = self.grid[i][j].move(self)    

                            # for each of those coordinate pairs, create new board
                            for x in newMovesCoords:
                                tempBoard = Board(copy.deepcopy(self.grid))
                                tempBoard.grid[x[0]][x[1]] = tempBoard.grid[i][j]
                                tempBoard.grid[x[0]][x[1]].i = x[0]         # do we need this elsewhere???
                                tempBoard.grid[x[0]][x[1]].j = x[1]
                                tempBoard.grid[i][j] = None
                                tempBoard.evalValue = tempBoard.evaluationFunction()
                                boardList.append(copy.deepcopy(tempBoard))
        if(strategy == 2):
            queenMoves = []
            bishopMoves = []
            rookMoves = []
            knightMoves = []
            kingMoves = []
            pawnMoves = []
            for i in range(8):
                for j in range(8):
                    if(self.grid[i][j] != None):
                        if(self.grid[i][j].color == 'b'):  # all white pieces
                            
                            # coordinates where we are moving a particular piece
                            newMovesCoords = self.grid[i][j].move(self)    

                            # for each of those coordinate pairs, create new board
                            for x in newMovesCoords:
                                tempBoard = Board(copy.deepcopy(self.grid))
                                tempBoard.grid[x[0]][x[1]] = tempBoard.grid[i][j]
                                tempBoard.grid[x[0]][x[1]].i = x[0]         # do we need this elsewhere???
                                tempBoard.grid[x[0]][x[1]].j = x[1]
                                tempBoard.grid[i][j] = None
                                tempBoard.evalValue = tempBoard.evaluationFunction()
                                if(self.grid[i][j].id == 'q'):
                                    queenMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'b'):
                                    bishopMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'r'):
                                    rookMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'n'):
                                    knightMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'k'):
                                    kingMoves.append(copy.deepcopy(tempBoard))
                                elif(self.grid[i][j].id == 'p'):
                                    pawnMoves.append(copy.deepcopy(tempBoard))
            for x in queenMoves:
                boardList.append(x)
            for x in bishopMoves:
                boardList.append(x)
            for x in rookMoves:
                boardList.append(x)
            for x in knightMoves:
                boardList.append(x)
            for x in kingMoves:
                boardList.append(x)
            for x in pawnMoves:
                boardList.append(x)

        return(boardList)





    # takes in a board, and prints to output a character representation of that board
    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def printBoard(self):
        print("    ◘----------------◘")
        for i in range(0,8):
            print('    |', end = '')
            for j in range(0,8):
                if(self.grid[i][j] == None):
                    print(" ", end = ' ')
                else:
                    print(self.grid[i][j].id, end = ' ')
            print('|', end = '')
            print()
        print("    ◘----------------◘")
