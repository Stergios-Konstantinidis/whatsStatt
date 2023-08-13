import whatsappAnalytics


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class Ui_List(object):
    def setupUi(self, List):
        self.credits = QtWidgets.QLabel(List)
        self.credits.setGeometry(QtCore.QRect(10, 500, 390, 40))
        self.credits.setObjectName("label")
        self.credits.setText("Stergios Konstantinidis ©2023; skonsta1@unil.ch; V1.0.0")

        self.button = QtWidgets.QPushButton(List)
        #self.button.setStyleSheet(“background-color : yellow”)
        self.button.setGeometry(QtCore.QRect(50, 10, 300, 30))
        self.button.setText("Cliquer ici pour importer la discution")
        self.button.clicked.connect(self.selectChat)

        self.buttonShowGraph = QtWidgets.QPushButton(List)
        self.buttonShowGraph.setGeometry(QtCore.QRect(20, 450, 220, 30))
        self.buttonShowGraph.setText("Cliquez ici pour afficher le graph")
        self.buttonShowGraph.clicked.connect(self.showGraph)

        self.nombreJours = QtWidgets.QLineEdit(List)
        self.nombreJours.setGeometry(QtCore.QRect(310, 455, 20, 20))
        self.nombreJours.setText("30")

        self.nombreJoursTxt = QtWidgets.QLabel(List)
        self.nombreJoursTxt.setGeometry(QtCore.QRect(330, 455, 40, 20))
        self.nombreJoursTxt.setText(" jours")
        self.nombreJoursTxt2 = QtWidgets.QLabel(List)
        self.nombreJoursTxt2.setGeometry(QtCore.QRect(245, 455, 100, 20))
        self.nombreJoursTxt2.setText("Graph sur ")
        

        self.listeResultat = QtWidgets.QListWidget(List)
        self.listeResultat.setGeometry(QtCore.QRect(20, 50, 360, 400))

        


    def selectChat(self):
       self.filename = QtWidgets.QFileDialog.getOpenFileName()
       scores = whatsappAnalytics.GetCount(self.filename[0])
       self.listeResultat.clear()
       self.listeResultat.addItems(scores)

    def showGraph(self):
      try:
        dateAnalitics = whatsappAnalytics.getDailyCount(self.filename[0], int(self.nombreJours.text()))
      except:
        self.selectChat()
        dateAnalitics = whatsappAnalytics.getDailyCount(self.filename[0], int(self.nombreJours.text()))

      dates = dateAnalitics[1]

      width = 0.6  # the width of the bars: can also be len(x) sequence
      fig, ax = plt.subplots()
      bottom = np.zeros(len(dates))
       
      for user, count in dateAnalitics[2].items():
            p = ax.bar(dates, count, width, label=user, bottom=bottom)
            bottom += count


            ax.bar_label(p, label_type='center')
            
      ax.set_title('messages par user')
      ax.legend()
      plt.show()



def launch():
  import sys
  app = QtWidgets.QApplication(sys.argv)
  List = QtWidgets.QDialog()
  ui = Ui_List()
  ui.setupUi(List)
  ui.on_user_selection()
  List.show()
  app.exec_()
  app.quit()

if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  List = QtWidgets.QDialog()
  ui = Ui_List()
  ui.setupUi(List)
  List.show()
  app.exec_()
  app.quit()