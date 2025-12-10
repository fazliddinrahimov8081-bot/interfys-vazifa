from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
import random

app = QApplication(sys.argv)

# --- Oyna yaratamiz ---
window = QWidget()
window.setWindowTitle("Random Son")
window.setGeometry(300, 300, 300, 200)

# --- Label ---
label = QLabel("Natija bu yerda chiqadi", window)
label.move(70, 50)
label.resize(200, 40)

# --- Tugma ---
btn = QPushButton("Son chiqarish", window)
btn.move(90, 100)

# Tugma bosilganda ishlaydigan funksiya
def show_random():
    son = random.randint(1, 100)
    label.setText(str(son))

# Tugmani funksiyaga ulaymiz
btn.clicked.connect(show_random)

window.show()
sys.exit(app.exec_())
