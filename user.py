#!/usr/bin/env python3
"""
Tic Tac Toe User or Player, which may be human or computer.
Author: Willisman31
Date: 6.3.2022

Tic Tac Toe user or player with known behaviors of every user; may be extended by other classes for automation of gameplay.
"""

class User:

    def __init__(self, symbol: str, name: str, board: Board) -> None:
        self.symbol = playSymbol
        self.name = name
        self.board = board

    def getSymbol(self) -> str:
        return self.symbol

    def setSymbol(self, playSymbol: str) -> None:
        self.symbol = playSymbol

    def getName(self) -> str:
        return self.name

    def setName(self, newName: str) -> None:
        self.name = newName



