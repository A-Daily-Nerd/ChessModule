def parseFEN(stringFEN: str):
    Lines = stringFEN.split("/")
    Board = []
    for i in Lines:
        for j in i:
            Board.append(j)
        Board.append("\n")
    return Board

def replaceIntWithChars(inputList: list):
    input_string = "".split(inputList)
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
        self.FEN  = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.Turn = 0
    def genBoard(self):
        Board = parseFEN(self.FEN)
        Board = replaceIntWithChars(Board)
        return ''.join(Board)

        
