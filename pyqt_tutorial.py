from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(1000, 200, 500, 300)
		self.setWindowTitle("Tech with Tim")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("my first label")
		self.label.move(100, 100)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click here!")
		self.b1.move(30, 30)
		self.b1.clicked.connect(self.clicked)

		self.button_counter = 1

	def clicked(self):
		self.label.setText(f"Button clicked {self.button_counter} times!")
		self.update()
		self.button_counter += 1

	def update(self):
		self.label.adjustSize()


def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())


window()
