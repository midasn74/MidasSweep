import random


class boardGenerator:
    def __init__(self, boardWidth: int, boardHeight: int, bombAmount: int):
        self.board = []

        self.gameStatus = None

        self.boardWidth = boardWidth

        self.boardHeight = boardHeight

        self.clearZerosChecked = []

        for a in range(boardHeight):
            tempList = []
            for b in range(self.boardWidth):
                tempList.append(0)
            self.board.append(tempList)

        self.gameBoard = []

        for a in range(boardHeight):
            tempList = []
            for b in range(self.boardWidth):
                tempList.append('h')
            self.gameBoard.append(tempList)

        self.bombs = []

        while bombAmount > 0:
            y = random.randint(0, (self.boardHeight - 1))
            x = random.randint(0, (self.boardWidth - 1))
            bomb = [y, x]
            bombAmount = bombAmount - 1
            if bomb in self.bombs:
                bombAmount = bombAmount + 1
            else:
                self.bombs.append(bomb)
                self.board[y][x] = 'b'

        for bomb in self.bombs:
            y = bomb[0]
            x = bomb[1]

            if y - 1 < 0:
                pass
            elif x - 1 < 0:
                pass
            elif self.board[y - 1][x - 1] == 'b':
                pass
            else:
                self.board[y - 1][x - 1] = self.board[y - 1][x - 1] + 1

            if y - 1 < 0:
                pass
            elif self.board[y - 1][x] == 'b':
                pass
            else:
                self.board[y - 1][x] = self.board[y - 1][x] + 1

            if y - 1 < 0:
                pass
            elif x + 1 > (self.boardWidth - 1):
                pass
            elif self.board[y - 1][x + 1] == 'b':
                pass
            else:
                self.board[y - 1][x + 1] = self.board[y - 1][x + 1] + 1

            if x - 1 < 0:
                pass
            elif self.board[y][x - 1] == 'b':
                pass
            else:
                self.board[y][x - 1] = self.board[y][x - 1] + 1

            if x + 1 > (self.boardWidth - 1):
                pass
            elif self.board[y][x + 1] == 'b':
                pass
            else:
                self.board[y][x + 1] = self.board[y][x + 1] + 1

            if x - 1 < 0:
                pass
            elif y + 1 > (self.boardHeight - 1):
                pass
            elif self.board[y + 1][x - 1] == 'b':
                pass
            else:
                self.board[y + 1][x - 1] = self.board[y + 1][x - 1] + 1

            if y + 1 > (self.boardHeight - 1):
                pass
            elif self.board[y + 1][x] == 'b':
                pass
            else:
                self.board[y + 1][x] = self.board[y + 1][x] + 1

            if x + 1 > (self.boardWidth - 1):
                pass
            elif y + 1 > (self.boardHeight - 1):
                pass
            elif self.board[y + 1][x + 1] == 'b':
                pass
            else:
                self.board[y + 1][x + 1] = self.board[y + 1][x + 1] + 1

    def getBombs(self):
        return self.bombs

    def getBoard(self):
        return self.board

    def clearZeros(self, y: int, x: int):
        if [y, x] in self.clearZerosChecked:
            pass
        else:
            self.clearZerosChecked.append([y, x])

            if y - 1 < 0:
                pass
            elif x - 1 < 0:
                pass
            elif self.board[y - 1][x - 1] == 0:
                self.gameBoard[y - 1][x - 1] = self.board[y - 1][x - 1]
                self.clearZeros(y - 1, x - 1)
            else:
                self.gameBoard[y - 1][x - 1] = self.board[y - 1][x - 1]

            if y - 1 < 0:
                pass
            elif self.board[y - 1][x] == 0:
                self.gameBoard[y - 1][x] = self.board[y - 1][x]
                self.clearZeros(y - 1, x)
            else:
                self.gameBoard[y - 1][x] = self.board[y - 1][x]

            if y - 1 < 0:
                pass
            elif x + 1 > (self.boardWidth - 1):
                pass
            elif self.board[y - 1][x + 1] == 0:
                self.gameBoard[y - 1][x + 1] = self.board[y - 1][x + 1]
                self.clearZeros(y - 1, x + 1)
            else:
                self.gameBoard[y - 1][x + 1] = self.board[y - 1][x + 1]

            if x - 1 < 0:
                pass
            elif self.board[y][x - 1] == 0:
                self.gameBoard[y][x - 1] = self.board[y][x - 1]
                self.clearZeros(y, x - 1)
            else:
                self.gameBoard[y][x - 1] = self.board[y][x - 1]

            if x + 1 > (self.boardWidth - 1):
                pass
            elif self.board[y][x + 1] == 0:
                self.gameBoard[y][x + 1] = self.board[y][x + 1]
                self.clearZeros(y, x + 1)
            else:
                self.gameBoard[y][x + 1] = self.board[y][x + 1]

            if x - 1 < 0:
                pass
            elif y + 1 > (self.boardHeight - 1):
                pass
            elif self.board[y + 1][x - 1] == 0:
                self.gameBoard[y + 1][x - 1] = self.board[y + 1][x - 1]
                self.clearZeros(y + 1, x - 1)
            else:
                self.gameBoard[y + 1][x - 1] = self.board[y + 1][x - 1]

            if y + 1 > (self.boardHeight - 1):
                pass
            elif self.board[y + 1][x] == 0:
                self.gameBoard[y + 1][x] = self.board[y + 1][x]
                self.clearZeros(y + 1, x)
            else:
                self.gameBoard[y + 1][x] = self.board[y + 1][x]

            if x + 1 > (self.boardWidth - 1):
                pass
            elif y + 1 > (self.boardHeight - 1):
                pass
            elif self.board[y + 1][x + 1] == 0:
                self.gameBoard[y + 1][x + 1] = self.board[y + 1][x + 1]
                self.clearZeros(y + 1, x + 1)
            else:
                self.gameBoard[y + 1][x + 1] = self.board[y + 1][x + 1]

    def getGameBoard(self):
        return self.gameBoard

    def isGameDone(self):
        hiddenItems = 0
        bombsLeft = 0

        for row in self.gameBoard:
            for item in row:
                if item == 'h':
                    hiddenItems = hiddenItems + 1

        for row in self.board:
            for item in row:
                if item == 'b':
                    bombsLeft = bombsLeft + 1

        if hiddenItems == bombsLeft:
            return True
        else:
            return False

    def step(self, y: int, x: int):
        hiddenSquare = self.board[y][x]

        if hiddenSquare == 'b':
            self.gameBoard[y][x] = hiddenSquare
            self.gameStatus = "L"
        elif hiddenSquare != 0:
            self.gameBoard[y][x] = hiddenSquare
            if self.isGameDone():
                self.gameStatus = "W"
            else:
                self.gameStatus = None
        else:
            self.gameBoard[y][x] = hiddenSquare
            self.clearZeros(y, x)
            self.clearZerosChecked = []
            if self.isGameDone():
                self.gameStatus = "W"
            else:
                self.gameStatus = None

        return self.gameStatus

    def flag(self, y: int, x: int):
        if self.gameBoard[y][x] == 'f':
            self.gameBoard[y][x] = 'h'
        elif self.gameBoard[y][x] != 'h':
            return
        else:
            self.gameBoard[y][x] = 'f'

    def unFlag(self, y: int, x: int):
        if self.gameBoard[y][x] != 'f':
            return
        else:
            self.gameBoard[y][x] = 'h'
