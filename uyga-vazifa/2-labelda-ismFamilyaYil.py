from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label va 3ta Button")
        self.setGeometry(200, 200, 350, 150)

        # Label
        self.label = QLabel("Ma'lumot kutilmoqda...", self)
        self.label.move(50, 30)
        self.label.resize(300, 30)

        # Buttonlar
        self.btn1 = QPushButton("Ism", self)
        self.btn1.move(30, 80)
        self.btn1.clicked.connect(self.show_name)

        self.btn2 = QPushButton("Familiya", self)
        self.btn2.move(120, 80)
        self.btn2.clicked.connect(self.show_surname)

        self.btn3 = QPushButton("Tug'ilgan sana", self)
        self.btn3.move(230, 80)
        self.btn3.clicked.connect(self.show_birth)

        # Tug'ilgan sana
        self.birth_date = (2004, 1, 28)  # yil, oy, kun

    def show_name(self):
        self.label.setText("Ism: Fazliddin")

    def show_surname(self):
        self.label.setText("Familiya: Rahimov")

    def show_birth(self):
        yil, oy, kun = self.birth_date
        self.label.setText(f"Tug'ilgan sana: {yil}-{oy:02d}-{kun:02d}")

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
