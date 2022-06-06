#!/usr/bin/env python3
"""
Tic Tac Toe Game Board
Author: Willisman31
Date: 6.3.2022

Class to create a dynamic and extensable tic-tac-toe game board
"""

class Board:

    def __init__(self, numberOfRows: int, numberOfColumns: int) -> None:
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.gameBoard = [[" "] * numberOfColumns] * numberOfRows

    # Used only for Command Line, not in GUI
    def displayBoard(self) -> str:
        display = ""
        for column in range(self.numberOfColumns * 2 - 1):
            for row in range(self.numberOfRows * 2 - 1):
                if row % 2 == 1:
                    if column % 2 == 1:
                        display += " "
                    else:
                        display += "|"
                else:
                    if column % 2 == 1:
                        display += "-"
                    else:
                        display += " "
            display += "\n"
        return display

    def getFieldValue(self, row, column) -> str:
        return self.gameBoard[row][column]


