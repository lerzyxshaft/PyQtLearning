from operator import is_not

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 22pt \".AppleSystemUIFont\";\n"
"\n"
"")
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(20)
        self.label.setObjectName("label")
        self.btn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(70, 185, 50, 50))
        self.btn_8.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.label_dvde = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_dvde.setGeometry(QtCore.QRect(190, 130, 50, 50))
        self.label_dvde.setStyleSheet("\n"
"background-color: rgb(255, 141, 14);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);")
        self.label_dvde.setObjectName("label_dvde")
        self.label_result = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(190, 350, 50, 50))
        self.label_result.setStyleSheet("\n"
"background-color: rgb(255, 141, 14);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.label_AC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_AC.setGeometry(QtCore.QRect(10, 130, 50, 50))
        self.label_AC.setStyleSheet("background-color: rgb(128, 128, 128);\n"
"\n"
"\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_AC.setObjectName("label_AC")
        self.label_minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_minus.setGeometry(QtCore.QRect(190, 240, 50, 50))
        self.label_minus.setStyleSheet("\n"
"background-color: rgb(255, 141, 14);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_minus.setObjectName("label_minus")
        self.label_mltpl = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_mltpl.setGeometry(QtCore.QRect(190, 185, 50, 50))
        self.label_mltpl.setStyleSheet("\n"
"background-color: rgb(255, 141, 14);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);")
        self.label_mltpl.setObjectName("label_mltpl")
        self.btn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(130, 185, 50, 50))
        self.btn_9.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.label_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_plus.setGeometry(QtCore.QRect(190, 295, 50, 50))
        self.label_plus.setStyleSheet("\n"
"background-color: rgb(255, 141, 14);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_plus.setObjectName("label_plus")
        self.label_pm = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_pm.setGeometry(QtCore.QRect(70, 130, 50, 50))
        self.label_pm.setStyleSheet("background-color: rgb(128, 128, 128);\n"
"\n"
"\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_pm.setObjectName("label_pm")
        self.label_prcnt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.label_prcnt.setGeometry(QtCore.QRect(130, 130, 50, 50))
        self.label_prcnt.setStyleSheet("background-color: rgb(128, 128, 128);\n"
"\n"
"\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_prcnt.setObjectName("label_prcnt")
        self.btn_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 185, 50, 50))
        self.btn_7.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_7.setObjectName("btn_7")
        self.btn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(10, 240, 50, 50))
        self.btn_2.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.btn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(70, 240, 50, 50))
        self.btn_5.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(130, 240, 50, 50))
        self.btn_6.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_6.setObjectName("btn_6")
        self.btn_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(130, 295, 50, 50))
        self.btn_4.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.btn_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(70, 295, 50, 50))
        self.btn_3.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.btn_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 295, 50, 50))
        self.btn_1.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.btn_calc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_calc.setGeometry(QtCore.QRect(10, 350, 50, 50))
        self.btn_calc.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_calc.setObjectName("btn_calc")
        self.btn_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(70, 350, 50, 50))
        self.btn_0.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_0.setObjectName("btn_0")
        self.btn_cma = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_cma.setGeometry(QtCore.QRect(130, 350, 50, 50))
        self.btn_cma.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(31, 31, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_cma.setObjectName("btn_cma")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.label_dvde.setText(_translate("MainWindow", "/"))
        self.label_result.setText(_translate("MainWindow", "="))
        self.label_AC.setText(_translate("MainWindow", "clear"))
        self.label_minus.setText(_translate("MainWindow", "-"))
        self.label_mltpl.setText(_translate("MainWindow", "*"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.label_plus.setText(_translate("MainWindow", "+"))
        self.label_pm.setText(_translate("MainWindow", "+/-"))
        self.label_prcnt.setText(_translate("MainWindow", "%"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_2.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "3"))
        self.btn_3.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_calc.setText(_translate("MainWindow", "calc"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_cma.setText(_translate("MainWindow", ","))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.label_dvde.clicked.connect(lambda: self.write_number(self.label_dvde.text()))
        self.label_plus.clicked.connect(lambda: self.write_number(self.label_plus.text()))
        self.label_minus.clicked.connect(lambda: self.write_number(self.label_minus.text()))
        self.label_mltpl.clicked.connect(lambda: self.write_number(self.label_mltpl.text()))
        self.label_result.clicked.connect(self.results)

    def write_number(self, number):
        if self.label.text() == "0" or self.is_equal:
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        res = eval(self.label.text())
        self.label.setText(str(res))
        self.is_equal = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


