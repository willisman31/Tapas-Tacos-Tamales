#!/usr/bin/env python3
"""
Tic Tac Toe Game Board
Author: Willisman31
Date: 6.3.2022

Class to create a dynamic and extensable tic-tac-toe game board
"""

class Board:

    def board(self, numberOfRows: int, numberOfColumns: int) -> none:
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.gameBoard = [[" "] * numberOfColumns] * numberOfRows

    def displayBoard(self) -> str:
        pass

    def getFieldValue(self, row, column) -> str:
        pass

    def setFieldValue(self, row, column) -> none:
        pass)

