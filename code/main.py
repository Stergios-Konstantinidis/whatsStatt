import whatsappAnalytics


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QDate
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg



class Ui_List(object):
    def setupUi(self, List):
        self.filename = None
        
      #boutons
        self.button = QtWidgets.QPushButton(List)
        #self.button.setStyleSheet(“background-color : yellow”)
        self.button.setGeometry(QtCore.QRect(50, 10, 300, 30))
        self.button.setText("Cliquer ici pour importer la discution")
        self.button.clicked.connect(self.selectChat)

        self.buttonShowGraph = QtWidgets.QPushButton(List)
        self.buttonShowGraph.setGeometry(QtCore.QRect(20, 490, 220, 30))
        self.buttonShowGraph.setText("Cliquez ici pour afficher le graph")
        self.buttonShowGraph.clicked.connect(self.showGraph)


      #limiter le nombre de jours de l'analyse
        self.plusieursJours = QtWidgets.QCheckBox(List)
        self.plusieursJours.setGeometry(QtCore.QRect(20, 60, 20, 20))
        self.plusieursJours.setTristate(False)
        self.plusieursJours.stateChanged.connect(self.limit)

        self.plusieursJoursTxt = QtWidgets.QLabel(List)
        self.plusieursJoursTxt.setGeometry(QtCore.QRect(40, 59, 230, 20))
        self.plusieursJoursTxt.setObjectName("label")
        self.plusieursJoursTxt.setText("Limiter l'analyse aux messages post : ")

        self.calendrier = QtWidgets.QDateEdit(List)
        self.calendrier.setDate(QDate(2000, 6, 1))
        self.calendrier.setGeometry(QtCore.QRect(270, 59, 100, 20))
        self.calendrier.dateChanged.connect(self.limit)

        
      #La liste des résultats
        self.listeResultat = QtWidgets.QListWidget(List)
        self.listeResultat.setGeometry(QtCore.QRect(20, 80, 360, 400))

      #Credits area
        self.credits = QtWidgets.QLabel(List)
        self.credits.setGeometry(QtCore.QRect(25, 520, 365, 40))
        self.credits.setObjectName("label")
        self.credits.setText("Stergios Konstantinidis ©2023; skonsta1@unil.ch; V1.0.0")

        


    def selectChat(self):
       if not self.plusieursJours.checkState():
         _qDate = QDate(2000,6,1)
       else:
          _qDate = self.calendrier.date()
      
       self.filename = QtWidgets.QFileDialog.getOpenFileName()
       scores = whatsappAnalytics.GetCount(self.filename[0], _qDate)
       self.listeResultat.clear()
       self.listeResultat.addItems(scores)

    def LimitSelectChat(self):
       if not self.plusieursJours.checkState():
         _qDate = QDate(2000,6,1)
       else:
          _qDate = self.calendrier.date()
       scores = whatsappAnalytics.GetCount(self.filename[0], _qDate)
       self.listeResultat.clear()
       self.listeResultat.addItems(scores)

    def showGraph(self):
      if not self.plusieursJours.checkState():
         _qDate = QDate(2000,6,1)
      else:
          _qDate = self.calendrier.date()
      try:
        dateAnalitics = whatsappAnalytics.getDailyCount(self.filename[0], _qDate)
      except:
        self.selectChat()
        dateAnalitics = whatsappAnalytics.getDailyCount(self.filename[0], _qDate)

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
    
    def limit(self):
      if self.filename == None:
        self.selectChat()
      else:
        self.LimitSelectChat()
    
          

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