#!/usr/bin/env python3
"""
Game and its logical flows
Author: Willisman31
Date: 6.3.2022

"""

class Game:

    
    symbolOptions = ["x", "o", "t", "l", "w", "r"]

    def __init__(self, numberOfRows: int, numberOfColumns: int, numberOfUsers: int) -> None:
        self.board = Board(numberOfRows, numberOfColumns)
        self.users = self.initializeUsers(numberOfUsers, board)

    def initializeUsers(self, numberOfUsers: int, board: Board) -> User[]:
        users = []
        for user in range(numberOfUsers):
            symbol = symbolOptions[numberOfUsers]
            defaultUserName = "User " + str(user + 1)
            users.append(User(defaultUserName, board, symbol))
        return users

    def play() -> None:
        pass

    def isWon() -> bool:
        pass

    def getNumberOfUsers(self) -> int:
        return self.users.length


