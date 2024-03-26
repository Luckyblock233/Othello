# This Python file uses the following encoding: utf-8
import Infomation as info

class Board:
    def __init__(self):
        self.block_num = info.kBlockNum
        self.block_size = info.kBlockSize
        self.margin = info.kMargin
        self.GetInitialBoard()





    def is_on_board(self, x, y):
        return 0 <= x and x < self.block_num and 0 <= y and y < self.block_num

    def is_end(self):
        white_position = self.GetLegalPosition(info.kWhite)
        black_position = self.GetLegalPosition(info.kBlack)

        return len(white_position) == 0 and len(black_position) == 0

    def get_winner(self):
        if not self.is_end():
            return -1, 0
        player_num = self.CountColorNum(info.player_color)
        ai_num = self.CountColorNum(info.ai_color)
        if player_num > ai_num:
            return info.player_color, abs(player_num - ai_num)
        elif ai_num > player_num:
            return info.ai_color, abs(player_num - ai_num)
        else:
            return info.kEmpryColor, 0

    def is_legal_position(self, x, y, color):
        return self.is_on_board(x, y) and self.board[x][y] == info.kEmpryColor and self.PlaceColor(x, y, color, True) != 0




    def GetInitialBoard(self):
        self.board = [[info.kEmpryColor] * self.block_num for x in range(self.block_num)]
        center = self.block_num // 2
        self.board[center - 1][center - 1] = info.kWhite
        self.board[center][center] = info.kWhite
        self.board[center - 1][center] = info.kBlack
        self.board[center][center - 1] = info.kBlack

    def CountColorNum(self, color):
        cnt = 0
        for i in self.board:
            for j in i:
                if j == color:
                    cnt += 1
        return cnt

    def GetLegalPosition(self, color):
        position = []
        for i in range(0, self.block_num):
            for j in range(0, self.block_num):
                if self.board[i][j] != 0:
                    continue
                if self.PlaceColor(i, j, color, True):
                    position.append((i, j))
        return position

    def PlaceColor(self, x, y, color, is_test=False):
        reversed_place = []
        opponent_color = info.opponent_color(color)
        self.board[x][y] = color
        for ex, ey in info.kDirection:
            nx, ny = x + ex, y + ey
            cnt = 0
            while self.is_on_board(nx, ny) and self.board[nx][ny] == opponent_color:
                nx, ny = nx + ex, ny + ey
                cnt = cnt + 1
            if (not self.is_on_board(nx, ny)) or (not self.board[nx][ny] == color) or (cnt == 0):
                continue
            while True:
                nx, ny = nx - ex, ny - ey
                reversed_place.append((nx, ny))
                if nx == x and ny == y:
                    break
        if is_test == True:
            self.board[x][y] = info.kEmpryColor
            return len(reversed_place)
        for nx, ny in reversed_place:
            self.board[nx][ny] = color
        return len(reversed_place)
