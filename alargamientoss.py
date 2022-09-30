# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:21:25 2022

@author: danie
"""

from PyQt5.QtWidgets import  QApplication, QTableWidgetItem, QMainWindow, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
import sys

import numpy as np
import Moduloss as md

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Grafico (FigureCanvas):
    def __init__(self, width=6, height=5, dpi=100): #Dots per inches (dpi) determines how many pixels the figure comprises. The default dpi in matplotlib is 100. 
        # se crea objeto figura 
        self.fig = Figure(figsize=(width, height), dpi=dpi) 
        self.axes = self.fig.add_subplot(1,1,1)
        #se llama el metodo para crear el primer grafico 
        self.compute_initial_figure()
        # se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)
        
    def compute_initial_figure(self):
         x = np.arange(0.0,20.0,1)
         y = np.arange(0.0,20.0,1)
         self.axes.plot(x,y) # el objeto axes es el que nos va a permitir hacer los graficos
         self.axes.legend(loc='best')
         self.axes.set_xlabel('x')
         self.axes.set_ylabel('y')
         self.axes.set_title('Gráfico')
         
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        loadUi('alargamientoo.ui',self)
        #Se llama a la rutina de configuracion
        self.setup()
    def setup(self):
        self.boton_graficar.clicked.connect(self.graficar_datos)
        self.boton_guardar.clicked.connect(self.cargarDatos)
        
        # los layout permiten organizar widgets en un contenedor 
        Layout=QHBoxLayout() # permite acomodar las graficas ya sea vertical u horizontal 
        self.campo_grafico.setLayout(Layout)
        #se crea un ojeto para el manejo de los graficos 
        self.sc1 = Grafico( width=6, height=5, dpi=100)
        
        # se añade el campo graficos 
        Layout.addWidget(self.sc1) 
    def cargarDatos(self):
        
        S=50 #mm2
        L0=100
        F=np.array([0,1394,2808,5686,7502,8221,9969,12979,14241,14483,13968,12625])
        L=np.array([100,100.03,100.08,100.13,100.2,100.25,100.64,101.91,103.18,104.45,105.72,106.99])
        # T=np.array([0,2.78*10**1,5.6160*10**1,1.1372*10**2,1.5004*10**2,1.6442*10**2,1.9938*10**2,2.5958*10**2,2.8482*10**2,2.8966*10**22.7936*10**2,2.5250*10**2])
        # au=np.array([0,3*10**-4,8*10**-4,1.3*10**-3,2*10**-3,2.5*10**-3,6.4*10**-3,1.91*10**-2,3.18*10**-2,4.45*10**-2,5.72*10**-2,6.99*10**-2])
        #Para la tensión
        T=md.tension(S,F)

        #Para el alargamiento unitario
        au=md.alargamiento(L,L0)
       
        

        self.tableWidget.setRowCount(len(F))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(('Fuerza','Longitud'))
        
        for i in range(0,len(F)):
            self.tableWidget.setItem(i,0,QTableWidgetItem(str(F[i])))
            self.tableWidget.setItem(i,1,QTableWidgetItem(str(L[i])))
            
        self.tableWidget2.setRowCount(len(F))
        self.tableWidget2.setColumnCount(2)
        self.tableWidget2.setHorizontalHeaderLabels(("Tensión",'Alargamiento (e)'))
         
        for i in range(0,len(F)):
             self.tableWidget2.setItem(i,0,QTableWidgetItem(str(T[i])))
             self.tableWidget2.setItem(i,1,QTableWidgetItem(str(au[i])))
            
    def graficar_datos(self):
        
        S=50 #mm2
        L0=100
        F=np.array([0,1394,2808,5686,7502,8221,9969,12979,14241,14483,13968,12625])
        L=np.array([100,100.03,100.08,100.13,100.2,100.25,100.64,101.91,103.18,104.45,105.72,106.99])
        #Para la tensión
        T=md.tension(S,F)

        #Para el alargamiento unitario
        au=md.alargamiento(L,L0)
        #se limpia los ejes del grafico
        self.sc1.axes.clear()
        
        T=md.tension(S,F)

        #Para el alargamiento unitario
        au=md.alargamiento(L,L0)         
       
        self.sc1.axes.plot(au,T)
        self.sc1.axes.set_xlabel('Alargamiento(e)')
        self.sc1.axes.set_ylabel('Tensión (N/mm2)')
        self.sc1.axes.set_title('Tensión vs alargamiento')
        self.sc1.axes.figure.canvas.draw() 
    def closeEvent(self, event):
          resultado= QMessageBox.question(self,"Salir...","¿Seguro que quieres salir?",
          QMessageBox.Yes | QMessageBox.No)
          if resultado == QMessageBox.Yes : 
              event.accept()
          else: 
             event.ignore()     
         

app=QApplication(sys.argv)
ppal=VentanaPrincipal()
ppal.show()
sys.exit(app.exec_())
         