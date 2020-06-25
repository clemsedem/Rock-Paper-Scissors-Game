import sys
from random import randint

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
computerScore = 0
playerScore = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(530, 150, 550, 500)
        self.setWindowTitle("Rock Paper Scissors Game")
        self.UI()

    def UI(self):
        #####################Scores###################
        self.scorecomputerText = QLabel("Computer Score: ", self)
        self.scorecomputerText.move(30, 20)
        self.scorecomputerText.setFont(textFont)

        self.scorePlayerText = QLabel("Player Score: ", self)
        self.scorePlayerText.move(330, 20)
        self.scorePlayerText.setFont(textFont)
        ####################################Images######################
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("images/rock-t.jpg"))
        self.imageComputer.move(90, 100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("images/rock-t.jpg"))
        self.imagePlayer.move(330, 100)

        self.imageGame = QLabel(self)
        self.imageGame.setPixmap(QPixmap("images/game1.png"))
        self.imageGame.move(240, 130)
        ###########################Buttons###################
        startBtn = QPushButton("Start", self)
        startBtn.setFont(buttonFont)
        startBtn.move(100, 250)
        startBtn.clicked.connect(self.start)
        stopBtn = QPushButton("Stop", self)
        stopBtn.setFont(buttonFont)
        stopBtn.clicked.connect(self.stop)
        stopBtn.move(290, 250)
        ###############################Timer##################
        self.timer = QTimer(self)
        self.timer.setInterval(70)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer = randint(1, 3)
        self.rndPlayer = randint(1, 3)

        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("images/rock-t.jpg"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("images/paper127.jpg"))
        else:
            self.imageComputer.setPixmap(QPixmap("images/scissors17.jpg"))

        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("images/rock-t.jpg"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("images/paper127.jpg"))
        else:
            self.imagePlayer.setPixmap(QPixmap("images/scissors17.jpg"))

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer == 1 and self.rndPlayer == 1:
            msgbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.rndComputer == 1 and self.rndPlayer == 2:
            msgbox = QMessageBox.information(self, "Information", "You Win!")
            playerScore += 1
            self.scorePlayerText.setText("Your Score:{}".format(playerScore))
        elif self.rndComputer == 1 and self.rndPlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "Computer Wins!")
            computerScore += 1
            self.scorecomputerText.setText("Computer Score:{}".format(computerScore))
            self.scorecomputerText.resize(200,20)
        elif self.rndComputer == 2 and self.rndPlayer == 1:
            msgbox = QMessageBox.information(self, "Information", "Computer Wins!")
            computerScore += 1
            self.scorecomputerText.setText("Computer Score:{}".format(computerScore))
            self.scorecomputerText.resize(200, 20)
        elif self.rndComputer == 2 and self.rndPlayer == 2:
            msgbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.rndComputer == 2 and self.rndPlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "You Win!")
            playerScore += 1
            self.scorePlayerText.setText("Your Score:{}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 1:
            msgbox = QMessageBox.information(self, "Information", "You Win!")
            playerScore += 1
            self.scorePlayerText.setText("Your Score:{}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 2:
            msgbox = QMessageBox.information(self, "Information", "Computer Wins!")

            computerScore += 1
            self.scorecomputerText.setText("Computer Score:{}".format(computerScore))
            self.scorecomputerText.resize(200, 20)
        elif self.rndComputer == 3 and self.rndPlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "Draw Game")

        if computerScore == 5:
            msgbox = QMessageBox.information(self, "Information", "Game Over!, You have lost")
            sys.exit()
        elif playerScore == 5:
            msgbox = QMessageBox.information(self, "Information", "Game Over!, You are the winner!")
            sys.exit()



def main():
    App = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet("background-color:khaki")
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
