from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulyator")
        self.setGeometry(200, 200, 300, 200)

        # LineEditlar
        self.num1_edit = QLineEdit(self)
        self.num1_edit.move(50, 20)
        self.num1_edit.resize(100, 30)

        self.num2_edit = QLineEdit(self)
        self.num2_edit.move(160, 20)
        self.num2_edit.resize(100, 30)

        # Natija label
        self.result_label = QLabel("Natija: ", self)
        self.result_label.move(50, 60)
        self.result_label.resize(200, 30)

        # Tugmalar
        self.add_btn = QPushButton("Qo'shish", self)
        self.add_btn.move(20, 100)
        self.add_btn.clicked.connect(self.add)

        self.sub_btn = QPushButton("Ayirish", self)
        self.sub_btn.move(100, 100)
        self.sub_btn.clicked.connect(self.subtract)

        self.mul_btn = QPushButton("Ko'paytirish", self)
        self.mul_btn.move(180, 100)
        self.mul_btn.clicked.connect(self.multiply)

        self.div_btn = QPushButton("Bo'lish", self)
        self.div_btn.move(100, 140)
        self.div_btn.clicked.connect(self.divide)

    def get_numbers(self):
        try:
            a = float(self.num1_edit.text())
            b = float(self.num2_edit.text())
            return a, b
        except ValueError:
            self.result_label.setText("Xato: Iltimos son kiriting")
            return None, None

    def add(self):
        a, b = self.get_numbers()
        if a is not None:
            self.result_label.setText(f"Natija: {a + b}")

    def subtract(self):
        a, b = self.get_numbers()
        if a is not None:
            self.result_label.setText(f"Natija: {a - b}")

    def multiply(self):
        a, b = self.get_numbers()
        if a is not None:
            self.result_label.setText(f"Natija: {a * b}")

    def divide(self):
        a, b = self.get_numbers()
        if a is not None:
            if b != 0:
                self.result_label.setText(f"Natija: {a / b}")
            else:
                self.result_label.setText("Xato: 0 ga bo'lib bo'lmaydi")

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())
