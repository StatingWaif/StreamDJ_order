from Twitchdj import Twitchdj
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
from PyQt5.QtCore import QThread
import os

class RequestThread(QThread):
	def __init__(self, ui, parent=None):
		super().__init__()
		self.ui = ui
		
	def run(self):
		addingSong(self.ui)

def addingSong(ui):
	dj_url = ui.StreamdjLabel.text()
	song_name = ui.MusicurlLabel.text()
	author_name = ui.AuthorLabel.text()

	if not 'streamdj.ru' in dj_url:
		dj_url = f'https://streamdj.ru/c/{dj_url}'
	if author_name == '':
		author_name = 'who am i?'
	
	try:
		channel = Twitchdj(dj_url)
		channel.add_song(song_name, author_name, ui)
	except:
		ui.LOGS.setText('Some kind of mistake')

def terminatingThread(thread):
	thread.terminate()
	thread.ui.LOGS.setText('Aborted')

def launch_addingSong(inst):
	inst.start()

if __name__ == '__main__':
	

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	RequestThread_instande = RequestThread(ui)



	try:	
		ui.OrderButton.clicked.connect(lambda: launch_addingSong(RequestThread_instande))
		ui.BreakButton.clicked.connect(lambda: terminatingThread(RequestThread_instande))
	except:
		ui.LOGS.setText('Some kind of mistake')
	
	sys.exit(app.exec_())



