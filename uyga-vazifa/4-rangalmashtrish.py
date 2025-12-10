from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QColor
import sys
import random

class ColorChanger(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rang almashtiruvchi dastur")
        self.setGeometry(200, 200, 300, 200)

        # Label
        self.label = QLabel("Salom!", self)
        self.label.move(100, 50)
        self.label.resize(100, 50)

        # Button
        self.button = QPushButton("Rangni o'zgartir", self)
        self.button.move(80, 120)
        self.button.clicked.connect(self.change_color)

        # Ranglar ro'yxati
        self.colors = ["red", "blue", "green", "yellow"]

    def change_color(self):
        new_color = random.choice(self.colors)
        self.label.setStyleSheet(f"color: {new_color}")

app = QApplication(sys.argv)
window = ColorChanger()
window.show()
sys.exit(app.exec_())
