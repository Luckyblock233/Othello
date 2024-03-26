# This Python file uses the following encoding: utf-8
import copy
import random

import Infomation as info
from Board import Board
from Node import Node


class AI:
    def __init__(self, color):
        self.max_try_time = info.kMaxAITryTimes
        self.color = color
        self.scalar = info.kScalar
        self.select_probability = info.kSelectPolicyProbability
        self.max_stimulate_times = info.kMaxStimulateTimes





    def Move(self, board):
        now_board = copy.deepcopy(board)
        root = Node(now_board, self.color)
        return self.UCTSearch(root)

    def UCTSearch(self, root):
        for i in range(self.max_try_time):
            leaf = self.SelectPolicy(root)
            reward = self.StimulatePolicy(leaf)
            self.Backup(leaf, reward)
            best_son = self.UCB(root, 0)
        return best_son.action

    def SelectPolicy(self, node):
        while not node.board.is_end():
            if len(node.sons) == 0:
                return self.Expand(node)
            elif random.uniform(0, 1) < self.select_probability:
                node = self.UCB(node, self.scalar)
            else:
                node = self.UCB(node, self.scalar)
                if not node.fully_expand():
                    return self.Expand(node)
                else:
                    node = self.UCB(node, self.scalar)
        return node

    def Expand(self, node):
        actions = node.board.GetLegalPosition(node.color)
        if len(actions) == 0:
            return node.father

        tried_action = [son.action for son in node.sons]
        not_tried_action = [a for a in actions if not a in tried_action]
        action = random.choice(not_tried_action)

        new_board = copy.deepcopy(node.board)
        new_board.PlaceColor(action[0], action[1], node.color)
        node.AddSon(new_board, action, info.opponent_color(node.color))
        return node.sons[-1]

    def UCB(self, node, scalar):
        max_value = -float('inf')
        best_son = []
        for son in node.sons:
            if son.visit_num == 0:
                best_son = [son]
                break
            value = info.ucb(node.visit_num, son.visit_num, son.reward, scalar)
            if value > max_value:
                best_son = [son]
                max_value = value
            elif value == max_value:
                best_son.append(son)
        if len(best_son) == 0:
            return node.father
        return random.choice(best_son)

    def StimulatePolicy(self, node):
        board = copy.deepcopy(node.board)
        color = node.color
        count = 0

        while not board.is_end() and count < self.max_stimulate_times:
            actions = board.GetLegalPosition(color)
            if not len(actions) == 0:
                action = random.choice(actions)
                board.PlaceColor(action[0], action[1], color)
                count = count + 1
            color = info.opponent_color(color)

        winner, delta = board.get_winner()
        if winner == info.player_color:
            return 0
        elif winner == info.ai_color and self.color == info.ai_color:
            return 100 + delta
        else:
            return -(100 + delta)


    def Backup(self, node, reward):
        while node != None:
            node.visit_num = node.visit_num + 1
            node.reward = node.reward + reward
            node = node.father
        return
