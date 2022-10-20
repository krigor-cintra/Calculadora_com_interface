# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt6UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from tratamento_dados import Operação_str
from botoes import *
from tratamento_dados import valor_digitado,apagar,função_definir_zero


class Ui_MainWindow(object):
    valordereserva = ""
    historico= ""
    visor=" "
    tipodeoperaçao=0
    op_virgula=False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Limpar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpar.setGeometry(QtCore.QRect(10, 130, 71, 61))
        self.Limpar.setObjectName("Limpar")
        self.Apagar = QtWidgets.QPushButton(self.centralwidget)
        self.Apagar.setGeometry(QtCore.QRect(90, 130, 71, 61))
        self.Apagar.setObjectName("Apagar")
        self.Porcentagem = QtWidgets.QPushButton(self.centralwidget)
        self.Porcentagem.setGeometry(QtCore.QRect(170, 130, 71, 61))
        self.Porcentagem.setObjectName("Porcentagem")
        self.dividir = QtWidgets.QPushButton(self.centralwidget)
        self.dividir.setGeometry(QtCore.QRect(250, 130, 71, 61))
        self.dividir.setObjectName("dividir")
        self.oito = QtWidgets.QPushButton(self.centralwidget)
        self.oito.setGeometry(QtCore.QRect(90, 200, 71, 61))
        self.oito.setObjectName("oito")

        self.Multiplicar = QtWidgets.QPushButton(self.centralwidget)
        self.Multiplicar.setGeometry(QtCore.QRect(250, 200, 71, 61))
        self.Multiplicar.setObjectName("Multiplicar")
        self.nove = QtWidgets.QPushButton(self.centralwidget)
        self.nove.setGeometry(QtCore.QRect(170, 200, 71, 61))
        self.nove.setObjectName("nove")
        self.sete = QtWidgets.QPushButton(self.centralwidget)
        self.sete.setGeometry(QtCore.QRect(10, 200, 71, 61))
        self.sete.setObjectName("sete")
        self.um = QtWidgets.QPushButton(self.centralwidget)
        self.um.setGeometry(QtCore.QRect(10, 340, 71, 61))
        self.um.setObjectName("um")
        self.dois = QtWidgets.QPushButton(self.centralwidget)
        self.dois.setGeometry(QtCore.QRect(90, 340, 71, 61))
        self.dois.setObjectName("dois")
        self.cinco = QtWidgets.QPushButton(self.centralwidget)
        self.cinco.setGeometry(QtCore.QRect(90, 270, 71, 61))
        self.cinco.setObjectName("cinco")
        self.tres = QtWidgets.QPushButton(self.centralwidget)
        self.tres.setGeometry(QtCore.QRect(170, 340, 71, 61))
        self.tres.setObjectName("tres")
        self.Soma = QtWidgets.QPushButton(self.centralwidget)
        self.Soma.setGeometry(QtCore.QRect(250, 340, 71, 61))
        self.Soma.setObjectName("Soma")
        self.subtrair = QtWidgets.QPushButton(self.centralwidget)
        self.subtrair.setGeometry(QtCore.QRect(250, 270, 71, 61))
        self.subtrair.setObjectName("subtrair")
        self.seis = QtWidgets.QPushButton(self.centralwidget)
        self.seis.setGeometry(QtCore.QRect(170, 270, 71, 61))
        self.seis.setObjectName("seis")
        self.quatro = QtWidgets.QPushButton(self.centralwidget)
        self.quatro.setGeometry(QtCore.QRect(10, 270, 71, 61))
        self.quatro.setObjectName("quatro")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(90, 410, 71, 61))
        self.zero.setObjectName("pushButton_17")
        self.igual = QtWidgets.QPushButton(self.centralwidget)
        self.igual.setGeometry(QtCore.QRect(250, 410, 71, 61))
        self.igual.setObjectName("igual")
        self.virgula = QtWidgets.QPushButton(self.centralwidget)
        self.virgula.setGeometry(QtCore.QRect(170, 410, 71, 61))
        self.virgula.setObjectName("virgula")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 410, 71, 61))
        self.pushButton_20.setObjectName("pushButton_20")
        self.Visor = QtWidgets.QLCDNumber(self.centralwidget)
        self.Visor.setGeometry(QtCore.QRect(10, 2, 311, 111))
        self.Visor.setObjectName("Visor")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 361, 541))
        self.frame.setStyleSheet("background-color: rgb(176, 152, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.Limpar.raise_()
        self.Apagar.raise_()
        self.Porcentagem.raise_()
        self.dividir.raise_()
        self.oito.raise_()
        self.Multiplicar.raise_()
        self.nove.raise_()
        self.sete.raise_()
        self.um.raise_()
        self.dois.raise_()
        self.cinco.raise_()
        self.tres.raise_()
        self.Soma.raise_()
        self.subtrair.raise_()
        self.seis.raise_()
        self.quatro.raise_()
        self.zero.raise_()
        self.igual.raise_()
        self.virgula.raise_()
        self.pushButton_20.raise_()
        self.Visor.raise_()

        self.nove.clicked.connect(lambda: self.retorno(algarismo9()))
        self.oito.clicked.connect(lambda:self.retorno(algarismo8()))
        self.sete.clicked.connect(lambda: self.retorno(algarismo7()))
        self.seis.clicked.connect(lambda: self.retorno(algarismo6()))
        self.cinco.clicked.connect(lambda: self.retorno(algarismo5()))
        self.quatro.clicked.connect(lambda: self.retorno(algarismo4()))
        self.tres.clicked.connect(lambda: self.retorno(algarismo3()))
        self.dois.clicked.connect(lambda: self.retorno(algarismo2()))
        self.um.clicked.connect(lambda: self.retorno(algarismo1()))
        self.zero.clicked.connect(lambda: self.retorno(algarismo0()))
        self.Limpar.clicked.connect(lambda: self.retorno_visor(0))
        self.Soma.clicked.connect(lambda: self.somar())
        self.Apagar.clicked.connect(lambda: self.apagar_dados())
        self.dividir.clicked.connect(lambda: self.divisao())
        self.Multiplicar.clicked.connect(lambda: self.multiplicacao())
        self.subtrair.clicked.connect(lambda: self.subtraicao())
        self.igual.clicked.connect(lambda:self.atc_igual())
        self.pushButton_20.clicked.connect(lambda: self.print_historico())
        self.virgula.clicked.connect(lambda:self.nvirgula())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Limpar.setText(_translate("MainWindow", "Clear"))
        self.Apagar.setText(_translate("MainWindow", "Delet"))
        self.Porcentagem.setText(_translate("MainWindow", "%"))
        self.dividir.setText(_translate("MainWindow", "/"))
        self.oito.setText(_translate("MainWindow", "8"))
        self.Multiplicar.setText(_translate("MainWindow", "*"))
        self.nove.setText(_translate("MainWindow", "9"))
        self.sete.setText(_translate("MainWindow", "7"))
        self.um.setText(_translate("MainWindow", "1"))
        self.dois.setText(_translate("MainWindow", "2"))
        self.cinco.setText(_translate("MainWindow", "5"))
        self.tres.setText(_translate("MainWindow", "3"))
        self.Soma.setText(_translate("MainWindow", "+"))
        self.subtrair.setText(_translate("MainWindow", "-"))
        self.seis.setText(_translate("MainWindow", "6"))
        self.quatro.setText(_translate("MainWindow", "4"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.igual.setText(_translate("MainWindow", "="))
        self.virgula.setText(_translate("MainWindow", "."))
        self.pushButton_20.setText(_translate("MainWindow", "?"))

    def retorno_visor(self,n):
        self.Visor.display(n)

    def retorno(self,n):
        if (self.op_virgula==True):
            self.op_virgula=False
            x = (str(valor_digitado(float(self.Visor.value()))))
            x=str(x).rstrip('0')+str(n)
            self.retorno_visor(str(x))
            return ((valor_digitado(self.Visor.value())))
        x = (str(valor_digitado(float(self.Visor.value())))).rstrip('0').rstrip(".")
        if (função_definir_zero(x)==True):
            x=""+str(n)
        else:
            x=str(x)+str(n)
        self.retorno_visor(str(x))
        return ((valor_digitado(self.Visor.value())))

    def pegar_dados_visor(self):
        return self.retorno("")


    def atc_igual(self):
        self.tipodeoperaçao = 0
        self.valordereserva = self.valordereserva + self.pegar_dados_visor()
        self.pegar_historico()
        self.retorno_visor(Operação_str(self.valordereserva))

    def pegar_historico(self):
        self.historico = str(self.historico) + str(self.valordereserva) + "\n"

    def getvalor_de_reserva(self):
        return self.valordereserva

    def setvalor_de_reserva(self,n):
        self.valordereserva=n
        return lambda: self.valordereserva

    def somar(self):
        if (self.realizar_operação()==True):
            self.tipodeoperaçao=1
            self.valordereserva = str(self.pegar_dados_visor())
            self.valordereserva = str(self.valordereserva)+"+"
            self.retorno_visor(0)
            return self.valordereserva
        else:
            self.tipodeoperaçao = 0
            self.valordereserva =self.valordereserva + self.pegar_dados_visor()
            self.retorno_visor(Operação_str(self.valordereserva))
            self.pegar_historico()
            self.somar()

    def subtraicao(self):
        if (self.realizar_operação() == True):
            self.tipodeoperaçao = 1
            self.valordereserva = str(self.pegar_dados_visor())
            self.valordereserva = str(self.valordereserva) + "-"
            self.retorno_visor(0)
            return self.valordereserva
        else:
            self.tipodeoperaçao = 0
            self.valordereserva = self.valordereserva + self.pegar_dados_visor()
            self.retorno_visor(Operação_str(self.valordereserva))
            self.pegar_historico()
            self.subtraicao()

    def multiplicacao(self):
        if (self.realizar_operação() == True):
            self.tipodeoperaçao = 1
            self.valordereserva = str(self.pegar_dados_visor())
            self.valordereserva = str(self.valordereserva) + "*"
            self.retorno_visor(0)
            return self.valordereserva
        else:
            self.tipodeoperaçao = 0
            self.valordereserva = self.valordereserva + self.pegar_dados_visor()
            self.retorno_visor(Operação_str(self.valordereserva))
            self.pegar_historico()
            self.multiplicacao()

    def divisao(self):
        if (self.realizar_operação() == True):
            self.tipodeoperaçao = 1
            self.valordereserva = str(self.pegar_dados_visor())
            self.valordereserva = str(self.valordereserva) + "/"
            print(self.valordereserva)
            self.retorno_visor(0)
            return self.valordereserva
        else:
            self.tipodeoperaçao = 0
            self.valordereserva = self.valordereserva + self.pegar_dados_visor()
            self.retorno_visor(Operação_str(self.valordereserva))
            self.pegar_historico()
            self.divisao()

    def print_historico(self):
        print(self.historico)

    def realizar_operação(self):
        if (self.tipodeoperaçao == 0):

            return True
        else:
            return False

    def apagar_dados(self):
        valor=((self.pegar_dados_visor()))
        valor1= apagar(valor)
        self.retorno_visor(valor1)
    def nvirgula(self):
        self.op_virgula=True
        x = (str(valor_digitado(float(self.Visor.value())))).rstrip('0')
        print(x)
        self.retorno_visor((x))
        print(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
