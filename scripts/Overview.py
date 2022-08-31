# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Overview.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import webbrowser
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QApplication
import ctypes
import sys
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
sys.path.append("./")
from Methods.Database import Database

class Ui_Overview(object):

    def setupUi(self, Overview):
        Overview.setObjectName("Overview")
        Overview.resize(1056, 800)

        self.centralwidget = QtWidgets.QWidget(Overview)
        self.centralwidget.setObjectName("centralwidget")
        
        self.itemDropMenu = QtWidgets.QComboBox(self.centralwidget)
        self.itemDropMenu.setGeometry(QtCore.QRect(20, 20, 851, 61))
        self.itemDropMenu.setObjectName("itemDropMenu")
        
        self.btnPrintData = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrintData.setGeometry(QtCore.QRect(890, 20, 121, 61))
        self.btnPrintData.setObjectName("btnPrintData")
        self.btnPrintData.setStyleSheet("background-color: rgb(170, 255, 255);")

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(20, 740, 70, 40,))
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setStyleSheet("background-color: rgb(170, 255, 255);")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 120, 321, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setFrameStyle( QFrame.Box)
        self.frame.setStyleSheet("#frame {border: 0.5px solid grey;}")
        
        self.lblLowest = QtWidgets.QLabel(self.frame)
        self.lblLowest.setGeometry(QtCore.QRect(10, 20, 71, 41))
        self.lblLowest.setObjectName("lblLowest")
        
        self.lblLowestOutput = QtWidgets.QLabel(self.frame)
        self.lblLowestOutput.setGeometry(QtCore.QRect(80, 20, 231, 41))
        self.lblLowestOutput.setText("")
        self.lblLowestOutput.setObjectName("lblLowestOutput")
        
        self.lblHighest = QtWidgets.QLabel(self.frame)
        self.lblHighest.setGeometry(QtCore.QRect(10, 70, 71, 41))
        self.lblHighest.setObjectName("lblHighest")
        
        self.lblHighestOutput = QtWidgets.QLabel(self.frame)
        self.lblHighestOutput.setGeometry(QtCore.QRect(80, 70, 231, 41))
        self.lblHighestOutput.setText("")
        self.lblHighestOutput.setObjectName("lblHighestOutput")
        
        self.lblDifference = QtWidgets.QLabel(self.frame)
        self.lblDifference.setGeometry(QtCore.QRect(10, 120, 61, 41))
        self.lblDifference.setObjectName("lblDifference")
        
        self.lblDifferenceOutput = QtWidgets.QLabel(self.frame)
        self.lblDifferenceOutput.setGeometry(QtCore.QRect(70, 120, 241, 41))
        self.lblDifferenceOutput.setText("")
        self.lblDifferenceOutput.setObjectName("lblDifferenceOutput")
        
        self.lblAlltimeLow = QtWidgets.QLabel(self.frame)
        self.lblAlltimeLow.setGeometry(QtCore.QRect(10, 170, 111, 41))
        self.lblAlltimeLow.setObjectName("lblAlltimeLow")
        
        self.lblAlltimeLowOutput = QtWidgets.QLabel(self.frame)
        self.lblAlltimeLowOutput.setGeometry(QtCore.QRect(120, 170, 191, 41))
        self.lblAlltimeLowOutput.setText("")
        self.lblAlltimeLowOutput.setObjectName("lblAlltimeLowOutput")
        
        self.lblAlltimeHigh = QtWidgets.QLabel(self.frame)
        self.lblAlltimeHigh.setGeometry(QtCore.QRect(10, 220, 111, 41))
        self.lblAlltimeHigh.setObjectName("lblAlltimeHigh")
        
        self.lblAlltimeHighOutput = QtWidgets.QLabel(self.frame)
        self.lblAlltimeHighOutput.setGeometry(QtCore.QRect(120, 220, 191, 41))
        self.lblAlltimeHighOutput.setText("")
        self.lblAlltimeHighOutput.setObjectName("lblAlltimeHighOutput")
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 430, 321, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFrameShape(0)
        self.scrollArea.setStyleSheet("#scrollArea {border: 0.5px solid grey;}")
 
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 319, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.btnPrintData.clicked.connect(self.printData)
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(390, 120, 621, 601))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("border: 0.5px solid grey;")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.widget.setLayout(self.layout)



        

        Overview.setCentralWidget(self.centralwidget)
        self.retranslateUi(Overview)
        QtCore.QMetaObject.connectSlotsByName(Overview)

        #Set items to itemDropMenu
        self.setItems()
        self.btnBack.clicked.connect(Overview.close)

    def retranslateUi(self, Overview):
        _translate = QtCore.QCoreApplication.translate
        Overview.setWindowTitle(_translate("Overview", "MainWindow"))
        self.btnPrintData.setText(_translate("Overview", "Print data"))
        self.btnBack.setText(_translate("Overview", "Back"))
        self.lblLowest.setText(_translate("Overview", "Lowest price: "))
        self.lblHighest.setText(_translate("Overview", "Highest price:"))
        self.lblDifference.setText(_translate("Overview", "Difference:"))
        self.lblAlltimeLow.setText(_translate("Overview", "All Time Lowest price:"))
        self.lblAlltimeHigh.setText(_translate("Overview", "All Time Highest price:"))


    #Tavaroiden nimien haku tietokannasta
    def setItems(self):
        itemNameList = Database.getItemNames()
        self.itemDropMenu.clear()
        self.itemDropMenu.setPlaceholderText(" ")
        self.itemDropMenu.setCurrentIndex(-1)

        correctItemList = []

        for item in itemNameList:
            if item[0] in correctItemList:
                pass
            else:
                correctItemList.append(item[0])


        for row in correctItemList:
            self.itemDropMenu.addItem(row)

    #Metodi datan printtaamiseen
    def printData(self):
        if self.itemDropMenu.currentText() == '':
            self.Mbox("Error","Item not selected", 0)
        else:
            self.scrollAreaWidgetContents.close()
            self.setChart()
            self.addButtons()
            self.setStats()
            

    #Metodilla lisätään tavaralle napit joista voi mennä tavaran sivuille tai poistaa sen
    def addButtons(self):
        
        #Avaa selaimen annetulla URL-osoitteella
        def openBrowser(url):
            webbrowser.open(url)
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 319, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        lblX, btn1X, btn2X, btnY = 30, 140, 240, 30
        shopIndex = 0

        QApplication.processEvents()
        itemName = self.itemDropMenu.currentText()
        shopName = Database.getShopNamesByItem(itemName)     

        for shop in shopName:
            url = Database.getURL(itemName)[shopIndex][0]
            lblShop = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            lblShop.setGeometry(lblX, btnY, 100, 35)
            lblShop.setText(str(shop[0]))
            lblShop.show()

            btnLink = QtWidgets.QPushButton("View item in shop", self.scrollAreaWidgetContents)
            btnLink.setGeometry(btn1X, btnY, 90, 35)
            btnLink.clicked.connect(lambda x, url2=url:openBrowser(url2))
            btnLink.setStyleSheet('background: PaleGreen')
            btnLink.show()

            btnDelete = QtWidgets.QPushButton("Delete item", self.scrollAreaWidgetContents)
            btnDelete.setGeometry(btn2X, btnY, 70, 35)
            btnDelete.setStyleSheet('background: #E74C3C')
            btnDelete.clicked.connect(lambda x, shop=shop: self.deleteButtonAction(itemName, shop))
            btnDelete.show()
        
            btnY += 65 
            shopIndex += 1

    #Metodi lisää tavaran hintatiedot
    def setStats(self):
        try:
            QApplication.processEvents()
            itemName = self.itemDropMenu.currentText()
      
            shopCount = Database.getShopCount(itemName)

            stats = Database.getCurrentPrices(itemName, shopCount)

            lowestPrice = min(stats)
            highestPrice = max(stats)

            difference = highestPrice[0] - lowestPrice[0]
            differencePercentage = round((highestPrice[0] / lowestPrice[0] - 1) * 100, 2)

            self.lblLowestOutput.setText(str(lowestPrice[0]) + " - " +str(lowestPrice[1]))
            self.lblHighestOutput.setText(str(highestPrice[0]) + " - " + str(highestPrice[1]))
            self.lblDifferenceOutput.setText(str(difference) + " (+" + str(differencePercentage) +"%)")

            getAlltimeLowest = Database.getLowestPriceAlltime(itemName)
            getAlltimeHighest = Database.getHighestPriceAlltime(itemName)

            lowestAlltimePrice = getAlltimeLowest[0][0]
            lowestAlltimePriceShop = getAlltimeLowest[0][1]
            highestAlltimePrice = getAlltimeHighest[0][0]
            highestAlltimePriceShop = getAlltimeHighest[0][1]

            self.lblAlltimeLowOutput.setText(str(lowestAlltimePrice) + " - " + str(lowestAlltimePriceShop))
            self.lblAlltimeHighOutput.setText(str(highestAlltimePrice) + " - " + str(highestAlltimePriceShop))

        except:
            self.setItems()
            self.lblLowestOutput.setText(" ")
            self.lblHighestOutput.setText(" ")
            self.lblDifferenceOutput.setText(" ")
            self.lblAlltimeLowOutput.setText(" ")
            self.lblAlltimeHighOutput.setText(" ")


    #Metodi ilmoitusikkunoiden tekoon
    def Mbox(self, title, text, style):
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        
    #Metodilla poistetaan tavaralta kauppa
    def deleteButtonAction(self, itemName, shop):
            Database.deleteItemPrices(Database, itemName, shop[0])
            Database.deleteItem(Database, itemName, shop[0])
            self.Mbox("Item deleted","Item deleted from shop: " + shop[0], 0)
            self.addButtons()
            self.setStats()

    #Graafin teko
    def setChart(self):
        QApplication.processEvents()
        itemName = self.itemDropMenu.currentText()
        itemShops = Database.getShopNamesByItem(itemName)
        shops = []
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        for shop in itemShops:
            list = []
            shop = shop[0]
            list.append(shop)

            x = Database.getItemPrices(itemName, shop)
            for y in x:
                list.append(y[0])
                list.append(y[1])

            shops.append(list)


        for x in range (len(itemShops)):

            shopName = ""
            price = []
            date = []
            for y in range (len(shops[x])):
                if y > 0:
                    if (y % 2) != 0:
                        price.append(shops[x][y])

                    else:
                        date.append(shops[x][y])

                else:
                    shopName = shopName + shops[x][y]

        
            ax.plot(date,price, label = shopName)
            ax.tick_params(labelrotation = 30)
            ax.yaxis.set_major_locator(MultipleLocator(25))
            ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                ncol=3, fancybox=True, shadow=True)
            self.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Overview = QtWidgets.QMainWindow()
    ui = Ui_Overview()
    ui.setupUi(Overview)
    Overview.show()
    sys.exit(app.exec_())