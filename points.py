import sys
import os
from random import randint
from PyQt5 import QtCore
from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QPainter,QPen)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
							 QGridLayout, QVBoxLayout, QHBoxLayout,QPushButton,
							 QLabel, QLineEdit, QPushButton,QMainWindow,QDesktopWidget,QWidget)


#
# Ce programme permet de faire 1 points rouge à côté de 1 000, 10 000 ou 100 000 points noirs
# dans le but de représenter visuellement ce que signifie un cas sur 100 000.
#



class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'Programme qui génère des points noirs'

		self.nbPointsNoirs = 0
		self.eventByButton = False

		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.showMaximized()

		self.width = self.frameGeometry().width()
		self.height = self.frameGeometry().height()


		layoutPrincipal = QGridLayout()
		layoutPrincipal.setColumnStretch(0, 25)
		layoutPrincipal.setColumnStretch(1, 1)

		widgetboutons = self.boutons()


		layoutPrincipal.addWidget(widgetboutons,0,1)

		self.setLayout(layoutPrincipal)

		self.show()


	def paintEvent(self,event):

		if self.eventByButton == True:
			self.eventByButton = False

			self.width = self.frameGeometry().width()
			self.height = self.frameGeometry().height()

			painter = QPainter()
			painter.begin(self)

			myPen = QPen()

			for i in range(self.nbPointsNoirs):
				myPen.setColor(Qt.black)
				myPen.setBrush(Qt.black)
				painter.setPen(myPen)
				calcul_taille_bordure_gauche = int(30/1366 * self.width)
				calcul_taille_bordure_droite = int(self.width - 166)	#166 : 1366-1200 : taille de la bordure sur mon écran
				calcul_taille_bordure_haut = calcul_taille_bordure_gauche
				calcul_taille_bordure_bas = int(665/728 * self.height)

				x = randint(calcul_taille_bordure_gauche,int(calcul_taille_bordure_droite))
				y = randint(calcul_taille_bordure_haut,calcul_taille_bordure_bas) 

				painter.drawRect(x,y,1,1)
			
			myPen.setColor(Qt.red)
			myPen.setBrush(Qt.red)

			x = randint(calcul_taille_bordure_gauche,int(calcul_taille_bordure_droite))
			y = randint(calcul_taille_bordure_haut,calcul_taille_bordure_bas) 
			print(x,y)
			painter.setPen(myPen)
			painter.drawRect(x,y,1,1)

			myPen.setWidth(5)
			painter.setPen(myPen)
			painter.drawEllipse(x-15,y-15,30,30)

			painter.end()


	def boutons(self):
		widget = QWidget()
		layout = QVBoxLayout()

		bouton10 = QPushButton("10")
		bouton10.clicked.connect(lambda: self.bouton(10))

		bouton100 = QPushButton("100")
		bouton100.clicked.connect(lambda: self.bouton(100))

		bouton1k = QPushButton("1 000")
		bouton1k.clicked.connect(lambda: self.bouton(1000))

		bouton10k = QPushButton("10 000")
		bouton10k.clicked.connect(lambda: self.bouton(10000))

		bouton100k = QPushButton("100 000")
		bouton100k.clicked.connect(lambda: self.bouton(100000))


		layout.addWidget(bouton10)
		layout.addWidget(bouton100)
		layout.addWidget(bouton1k)
		layout.addWidget(bouton10k)
		layout.addWidget(bouton100k)

		widget.setLayout(layout)
		return widget

	@QtCore.pyqtSlot()
	def bouton(self,nbPointsNoirs):
		self.nbPointsNoirs = nbPointsNoirs
		self.eventByButton = True
		self.update()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
