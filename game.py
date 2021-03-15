from midasSweeper import boardGenerator
import tkinter
import time
from functools import partial

def runGame(game):
    gameWindow = tkinter.Tk()
    gameWindow.configure(background="white")
    gameWindow.title("Midas Sweeper")

    def killGameWindow():
        gameWindow.destroy()

    def stepTkinter(y, x):
        step = game.step(y, x)

        if step == None:
            pass
        elif step == "W":
            print("You won")
            killGameWindow()
        elif step == "L":
            print("You lost")
            killGameWindow()
            
        rowCount = 0
        columnCount = -1

        for row in game.gameBoard:
            rowCount = rowCount + 1
            for item in row:
                columnCount = columnCount + 1

                #leftClick = partial(stepTkinter, (rowCount - 1), columnCount)

                #rightClick = partial(stepTkinter, (rowCount - 1), columnCount)

                button = tkinter.Button(gameWindow, width=4, height=2)
                button.grid(row=rowCount, column=columnCount, sticky=tkinter.W)

                button.bind("<Button-1>", lambda event, y=(rowCount - 1), x=columnCount: stepTkinter(y, x))
                button.bind("<Button-2>", lambda event, y=(rowCount - 1), x=columnCount: flagTkinter(y, x))
                button.bind("<Button-3>", lambda event, y=(rowCount - 1), x=columnCount: flagTkinter(y, x))

                if item == 'b':
                    button["bg"] = "red"

                elif item == 'h':
                    button["text"] = ""
                    button["bg"] = "white"
                elif item == 'f':
                    button["text"] = "🏳"
                    button["bg"] = "orange"
                elif item == 0:
                    button["text"] = ""
                    button["bg"] = "gray"
                else:
                    button["text"] = item
                    button["fg"] = "green"
                    button["bg"] = "white"

            columnCount = -1

    def flagTkinter(y, x):
        game.flag(y, x)
            
        rowCount = 0
        columnCount = -1

        for row in game.gameBoard:
            rowCount = rowCount + 1
            for item in row:
                columnCount = columnCount + 1

                #leftClick = partial(stepTkinter, (rowCount - 1), columnCount)

                #rightClick = partial(stepTkinter, (rowCount - 1), columnCount)

                button = tkinter.Button(gameWindow, width=4, height=2)
                button.grid(row=rowCount, column=columnCount, sticky=tkinter.W)

                button.bind("<Button-1>", lambda event, y=(rowCount - 1), x=columnCount: stepTkinter(y, x))
                button.bind("<Button-2>", lambda event, y=(rowCount - 1), x=columnCount: flagTkinter(y, x))
                button.bind("<Button-3>", lambda event, y=(rowCount - 1), x=columnCount: flagTkinter(y, x))

                if item == 'b':
                    button["bg"] = "red"

                elif item == 'h':
                    button["text"] = ""
                    button["bg"] = "white"
                elif item == 'f':
                    button["text"] = "🏳"
                    button["bg"] = "orange"
                elif item == 0:
                    button["text"] = ""
                    button["bg"] = "gray"
                else:
                    button["text"] = item
                    button["fg"] = "green"
                    button["bg"] = "white"

            columnCount = -1
    
    tkinter.Button(gameWindow, text="Stop", width=4, command=killGameWindow).grid(row=0, column=0, sticky=tkinter.W)

    rowCount = 0
    columnCount = -1

    for row in game.gameBoard:
        rowCount = rowCount + 1
        for item in row:
            columnCount = columnCount + 1

            #leftClick = partial(stepTkinter, (rowCount - 1), columnCount)

            #rightClick = partial(stepTkinter, (rowCount - 1), columnCount)

            button = tkinter.Button(gameWindow, width=4, height=2)
            button.grid(row=rowCount, column=columnCount, sticky=tkinter.W)
            button.bind("<Button-1>", lambda event, y=(rowCount - 1), x=columnCount: stepTkinter(y, x))
            button.bind("<Button-2>", lambda event, y=(rowCount - 1), x=columnCount: flagTkinter(y, x))
            button.bind("<Button-3>", lambda event, y=(rowCount - 1), x=columnCount: flagTkinter(y, x))
        columnCount = -1

    gameWindow.mainloop()

def submitClick():
    boardHeight = inputBoardHeight.get()
    boardWidth = inputBoardWidth.get()
    bombAmount = inputBombAmount.get()
    game = boardGenerator(boardHeight=int(boardHeight), boardWidth=int(boardWidth), bombAmount=int(bombAmount))
    window.destroy()
    runGame(game)

window = tkinter.Tk()
window.configure(background="white")
window.title("Midas Sweeper")

tkinter.Label(window, text="Enter the height of the board.", bg="white", fg="black", font="none 12").grid(row=0, column=0, sticky=tkinter.W)

inputBoardHeight = tkinter.Entry(window, width=20, bg="white", font="none 12")
inputBoardHeight.grid(row=0, column=1, sticky=tkinter.W)

tkinter.Label(window, text="Enter the width of the board.", bg="white", fg="black", font="none 12").grid(row=1, column=0, sticky=tkinter.W)

inputBoardWidth = tkinter.Entry(window, width=20, bg="white", font="none 12")
inputBoardWidth.grid(row=1, column=1, sticky=tkinter.W)

tkinter.Label(window, text="Enter the amount of bombs in the game.", bg="white", fg="black", font="none 12").grid(row=2, column=0, sticky=tkinter.W)

inputBombAmount = tkinter.Entry(window, width=20, bg="white", font="none 12")
inputBombAmount.grid(row=2, column=1, sticky=tkinter.W)

tkinter.Button(window, text="Submit", width=6, command=submitClick).grid(row=3, column=0, sticky=tkinter.W)

window.mainloop()
