# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:10:04 2020

@author: Joaco
"""
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("Modelo3.ui", self)
        self.CalcularBo.clicked.connect(self.Masa)
        self.CalcularBo.clicked.connect(self.Calorias)
    

    #Masa Corporal
    def Masa(self):
        Peso=int(self.Pesocomb.currentText())
        Altura=float(self.Altcomb.currentText())
        M1=((Peso/Altura**2))
        M2=str("%.2f" %M1)
        self.Resultado1.setText(M2)
        
    #Descripcion de Masa
        if M1>=40:
            self.Resultado2.setText("Obesidad Morbida. Uregente mejorar")
            self.Resultado1_3.setText("5 Dias/Semana")
            self.Resultado2_3.setText("Caminatas, Aerobics, Zumba ligera")
        
        elif M1<=35 and M1>=39.9 :
            self.Resultado2.setText("Obesidad Severa. Urgente mejorar")
            self.Resultado1_3.setText("4 Dias/Semana")
            self.Resultado2_3.setText("Steps, caminata, Aerobics, Zumba")
        
        elif M1>=30 and M1<= 34.9:
            self.Resultado2.setText("Obesidad Moderada. Hay que mejorar")
            self.Resultado1_3.setText("4 Dias/Semana")
            self.Resultado2_3.setText("Trotar, Aerobics, Steps, Zumba")
    
        elif M1>=25 and M1<= 29.9:
            self.Resultado2.setText("Sobrepeso. Pero se puede mejorar")
            self.Resultado1_3.setText("5 Dias/Semana")
            self.Resultado2_3.setText("Ciclismo, Cuerda, Trotar, Zumba")
        
        elif M1>=18.5 and M1<= 24.9:
            self.Resultado2.setText("En hora buena peso Saludable")
            self.Resultado1_3.setText("6 Dias/Semana")
            self.Resultado2_3.setText("Pesas, Crosfit , Yoga, Sprint")
        
        elif M1>=16 and M1<=18.4:
            self.Resultado2.setText("Delgadez. Necesitas Masa moscular")
            self.Resultado1_3.setText("5 Dias/Semana")
            self.Resultado2_3.setText("Pesas, Pierna, Mancuernas, Crosfit")
        
        elif M1>=15 and M1<=15.9:
            self.Resultado2.setText("Delgadez Severa. Hay que comer mas")
            self.Resultado1_3.setText("3 Dias/Semana")
            self.Resultado2_3.setText("Consultar Nutricionista antes")
        
        elif M1<=14.9:
            self.Resultado2.setText("Delgadez Muy Severa. Urgente mejorar")
            self.Resultado1_3.setText("3 Dias/Semana")
            self.Resultado2_3.setText("Consultar Nutricionista antes")
        
        else:
            self.Resultado2.setText("Faltan Datos")
            self.Resultado1_3.setText("Faltan Datos")
            self.Resultado2_3.setText("Faltan Datos")
    
    
    
    #Calorias Diarias
    def Calorias(self):
        Genero1=str(self.GenBox.currentText())
        Peso=int(self.Pesocomb.currentText())
        Altura=float(self.Altcomb.currentText())
        Edad=int(self.Edadcomb.currentText())
        Acti=str(self.ActBox.currentText())
  
        # Calorias Diarias Hombre      
        if Genero1=="M"and Acti=="Sedentario":
            C1=(66.4+(13.75*Peso)+(5*(Altura*100))-(6.7*Edad))*1.2
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Necesitas estar activo")
            
        elif Genero1=="M"and Acti=="Ligera":
            C1=(66.4+(13.75*Peso)+(5*(Altura*100))-(6.7*Edad))*1.3775
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Necesitas mas energia")
            
        elif Genero1=="M"and Acti=="Moderada":
            C1=(66.4+(13.75*Peso)+(5*(Altura*100))-(6.7*Edad))*1.55
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Nivel de Energia aceptable")
            
        elif Genero1=="M"and Acti=="Activo":
            C1=(66.4+(13.75*Peso)+(5*(Altura*100))-(6.7*Edad))*1.9
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Buen nivel de energia")

        # Calorias Diarias Mujer
        elif Genero1=="F"and Acti=="Sedentario":
            C1=665+(9.5*Peso)+(1.8*(Altura*100))-(4.6*Edad)*1.2
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Necesitas estar activo")

        elif Genero1=="F"and Acti=="Ligera":
            C1=665+(9.5*Peso)+(1.8*(Altura*100))-(4.6*Edad)*1.3775
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Necesitas mas energia")
            
        elif Genero1=="F"and Acti=="Moderada":
            C1=665+(9.5*Peso)+(1.8*(Altura*100))-(4.6*Edad)*1.55
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Nivel de Energia aceptable")
            
        elif Genero1=="F"and Acti=="Activo":
            C1=665+(9.5*Peso)+(1.8*(Altura*100))-(4.6*Edad)*1.9
            C2=str("%.3f" %C1)+" Kcal"
            self.Resultado1_2.setText(C2)
            self.Resultado2_2.setText("Buen nivel de energia")
            
        else:
            self.Resultado1_2.setText("Datos?")
            self.Resultado2_2.setText("Faltan Datos")
     
        
               
if __name__== "__main__":
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())



