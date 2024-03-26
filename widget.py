# This Python file uses the following encoding: utf-8
import os
import time
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QFrame
from PySide6.QtCore import Qt, QFile
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader

import Infomation as info
from Board import Board
from AI import AI

loader = QUiLoader()

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
#        self.setCursor(Qt.PointingHandCursor)
        self.ui.Button_remake.clicked.connect(self.GameStart)

    def load_ui(self):
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

    def mousePressEvent(self, e):
        if self.is_player_round == False:
            return
        y, x = e.x(), e.y()
        if e.button() == Qt.LeftButton:
            i = (x - self.board.margin) // self.board.block_size
            j = (y - self.board.margin) // self.board.block_size
            if self.board.is_legal_position(i, j, info.player_color) == False:
                return
            self.board.PlaceColor(i, j, info.player_color)
            self.Refresh()
            self.is_player_round = False
            self.Judge()
            if self.is_gaming == False:
                self.GameEnd()
                return
            elif self.is_player_round == False:
                self.AIMove()






    def GameStart(self):
        self.GameRemake()
        if self.is_player_round == False:
            self.AIMove()

    def Refresh(self):
#        for i in range(0, 8):
#            for j in range(0, 8):
#                print(self.board.board[i][j], end="")
#            print()
        pixmap_black = QPixmap("./black.png")
        pixmap_white = QPixmap("./white.png")
#        print(pixmap_black, pixmap_white)
        for i in range(self.board.block_num):
            for j in range(self.board.block_num):
                self.labels[i][j].setScaledContents(True)
                if self.board.board[i][j] == info.kBlack:
                    self.labels[i][j].setPixmap(pixmap_black)
#                    setText("黑黑黑黑")
                elif self.board.board[i][j] == info.kWhite:
                    self.labels[i][j].setPixmap(pixmap_white)
                else:
                    self.labels[i][j].clear()
        self.ui.Label_black_number.setText(str(self.board.CountColorNum(info.kBlack)))
        self.ui.Label_white_number.setText(str(self.board.CountColorNum(info.kWhite)))
        QApplication.processEvents()

    def GameInit(self):
        self.board = Board()
        self.labels = [[0] * self.board.block_num for x in range(self.board.block_num)]
        for i in range(self.board.block_num):
            for j in range(self.board.block_num):
                y = i * self.board.block_size + self.board.margin
                x = j * self.board.block_size + self.board.margin
                self.labels[i][j] = QLabel("", self)
                self.labels[i][j].setFrameShape(QFrame.Box)
                self.labels[i][j].setAlignment(Qt.AlignCenter)
                self.labels[i][j].setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);");
                self.labels[i][j].setGeometry(x, y, self.board.block_size, self.board.block_size)
                self.labels[i][j].setVisible(True)
                self.labels[i][j].show()

    def GameRemake(self):
        reply = QMessageBox.question(self,"选择颜色","是否选择执黑棋（先手）？",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            info.player_color = info.kBlack
        else:
            info.player_color = info.kWhite
        info.ai_color = info.opponent_color(info.player_color)

        self.board = Board()
        self.is_gaming = True
        self.is_player_round = (info.player_color == info.kBlack)
        self.Refresh()

    def AIMove(self):
        ai = AI(info.ai_color)
        action = ai.Move(self.board)
        self.board.PlaceColor(action[0], action[1], info.ai_color)
        self.Refresh()
        self.is_player_round = True
        self.Judge()
        if self.is_gaming == False:
            self.GameEnd()
            return
        elif self.is_player_round == False:
            self.AIMove()

    def Judge(self):
        if self.board.is_end() == True:
            self.is_gaming = False
            return

        legal_position = []
        if self.is_player_round == True:
            legal_position = self.board.GetLegalPosition(info.player_color)
        else:
            legal_position = self.board.GetLegalPosition(info.ai_color)
        if len(legal_position) == 0:
            QMessageBox.warning(self, "遗憾！", "当前玩家无法进行落子！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            self.is_player_round = not self.is_player_round

    def GameEnd(self):
        self.is_gaming = False
        winner, diffence = self.board.get_winner()
        reply = False
        if winner == info.player_color:
            reply = QMessageBox.question(self, "游戏结束","玩家获胜！\n是否重新开始？", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif winner == info.ai_color:
            reply = QMessageBox.question(self, "游戏结束","AI 获胜！\n是否重新开始？", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            reply = QMessageBox.question(self, "游戏结束","平局！\n是否重新开始？", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.GameStart()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setWindowTitle("Othello")
    widget.show()
    widget.GameInit()
    widget.GameStart()
    sys.exit(app.exec())
