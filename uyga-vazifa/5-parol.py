from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
import sys

class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parol tekshiruvchi")
        self.setGeometry(200, 200, 300, 150)

        # LineEdit (parol kiritish)
        self.line_edit = QLineEdit(self)
        self.line_edit.move(50, 30)
        self.line_edit.resize(200, 30)
        self.line_edit.setEchoMode(QLineEdit.Password)  # Kiritilgan parol yulduzcha bilan ko'rinadi

        # Button
        self.button = QPushButton("Tekshirish", self)
        self.button.move(100, 70)
        self.button.clicked.connect(self.check_password)

        # Label
        self.label = QLabel("", self)
        self.label.move(50, 110)
        self.label.resize(200, 30)

    def check_password(self):
        if self.line_edit.text() == "12345":
            self.label.setText("Parol to'g'ri")
        else:
            self.label.setText("Noto'g'ri parol")

app = QApplication(sys.argv)
window = PasswordChecker()
window.show()
sys.exit(app.exec_())
