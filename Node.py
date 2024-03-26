# This Python file uses the following encoding: utf-8
import Infomation as info
from Board import Board

class Node:
    def __init__(self, board, color, father=None, action=None):
        self.board = board
        self.color = color
        self.father = father
        self.action = action

        self.visit_num = 0
        self.reward = 0.0
        self.sons = []

    def AddSon(self, board, action, color):
        son = Node(board, color, self, action)
        self.sons.append(son)

    def fully_expand(self):
        action = self.board.GetLegalPosition(self.color)
        return len(self.sons) == len(action)
