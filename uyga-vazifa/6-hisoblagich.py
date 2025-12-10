from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hisoblagich")
        self.setGeometry(200, 200, 250, 150)

        # Dastlabki qiymat
        self.count = 0

        # Label
        self.label = QLabel(str(self.count), self)
        self.label.move(110, 40)
        self.label.resize(50, 30)

        # +1 tugma
        self.btn_plus = QPushButton("+1", self)
        self.btn_plus.move(40, 80)
        self.btn_plus.clicked.connect(self.increment)

        # -1 tugma
        self.btn_minus = QPushButton("-1", self)
        self.btn_minus.move(140, 80)
        self.btn_minus.clicked.connect(self.decrement)

    def increment(self):
        self.count += 1
        self.label.setText(str(self.count))

    def decrement(self):
        self.count -= 1
        self.label.setText(str(self.count))

app = QApplication(sys.argv)
window = CounterApp()
window.show()
sys.exit(app.exec_())
