from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

app = QApplication([])
window = QMainWindow()

button = QPushButton("Нажми меня!")
layout = QVBoxLayout()
layout.addWidget(button)

container = QWidget()
container.setLayout(layout)
window.setCentralWidget(container)

window.show()
app.exec()