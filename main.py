from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidget
from PyQt5 import uic
import sys
from api_pull import RickAndMorty
import webbrowser


class AnotherWindow(QListWidget):
    def __init__(self, name):
        super().__init__()
        self.rick_and_morty = RickAndMorty()
        self.resize(500, 500)
        self.setStyleSheet('font-size: 15px;')

        if name == "Rick":
            for chapter in self.rick_and_morty.all_rick_chapters():
                self.addItems(chapter)
            self.itemDoubleClicked.connect(lambda: self.double_clicked('rick'))
        elif name == "Morty":
            for chapter in self.rick_and_morty.all_morty_chapters():
                self.addItems(chapter)
            self.itemDoubleClicked.connect(
                lambda: self.double_clicked('morty'))
        elif name == "Summer":
            for chapter in self.rick_and_morty.all_summer_chapters():
                self.addItems(chapter)
            self.itemDoubleClicked.connect(
                lambda: self.double_clicked('summer'))
        elif name == "BirdPerson":
            for chapter in self.rick_and_morty.all_birdPerson_chapters():
                self.addItems(chapter)
            self.itemDoubleClicked.connect(
                lambda: self.double_clicked('birdperson'))

    def double_clicked(self, name):

        url = f"https://rickandmortyapi.com/api/character/?name={name}"
        print(f'nigger {name}')
        webbrowser.open(url, new=0, autoraise=True)


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("image.ui", self)

        self.button_1 = self.findChild(QPushButton, "pushButton")
        self.button_2 = self.findChild(QPushButton, "pushButton_2")
        self.button_3 = self.findChild(QPushButton, "pushButton_3")
        self.button_4 = self.findChild(QPushButton, "pushButton_4")

        self.button_1.setStyleSheet(
            "background-image : url(./images/rick.jpg);")
        self.button_2.setStyleSheet(
            "background-image : url(./images/morty.jpg);")
        self.button_3.setStyleSheet(
            "background-image : url(./images/summer.jpg);")
        self.button_4.setStyleSheet(
            "background-image : url(./images/birdperson.jpg);")

        self.button_1.clicked.connect(lambda: self.clicker1("Rick"))
        self.button_2.clicked.connect(lambda: self.clicker1("Morty"))
        self.button_3.clicked.connect(lambda: self.clicker1("Summer"))
        self.button_4.clicked.connect(lambda: self.clicker1("BirdPerson"))

        self.show()

    def clicker1(self, name):
        print(f'nigger {name}')
        self.aw = AnotherWindow(name=name)
        self.aw.show()


sys.setrecursionlimit(1000000)
app = QApplication(sys.argv)
Window = UI()
app.exec_()
