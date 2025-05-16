def parseSquare(square: str):
    squareDefs = {"a":0,
                  "b":1,
                  "c":2,
                  "d":3,
                  "e":4,
                  "f":5,
                  "g":6,
                  "h":7}
    try:
        file = int(square[1])
        rank = int(squareDefs[square[0]])
    except:
        return None
    else:
        position = ((9*file)+rank)-9
    return position

def parseFEN(stringFEN: str):
    Lines = stringFEN.split("/")
    Board = []
    for i in Lines:
        for j in i:
            Board.append(j)
        Board.append("\n")
    return Board

def replaceIntWithChars(inputList: list):
    input_string  = ''.join(inputList)
    result_string = ""
    for char in input_string:
        if char.isdigit():
            result_string += "#" * int(char)
        else:
            result_string += char
    return result_string


def genFEN(Board: list):
    i = 0
    for I in Board:
        if I == "\n":
            Board[i] = "/"
        i += 1
    Board = Board[0:len(Board)-1]
    FEN = "".join(Board)
    return FEN

class Board:
    def __init__(self):
        self.FEN  = "rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR"
        self.Turn = 0
    def __repr__(self):
        return f"<Chess board with position: {self.FEN}>"
    def getBoard(self):
        Board = parseFEN(self.FEN)
        Board = replaceIntWithChars(Board)
        return ''.join(Board)
    def getSquare(self,square: str):
        b = self.getBoard()[::-1]
        b = b[1:]
        b = b + "\n"
        return b[parseSquare(square)]
    def moveBasic(self,start: str,end: str):