# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from AddItem import Ui_AddItem
from AddShopForItem import Ui_AddShopForItem
from Overview import Ui_Overview
from datetime import datetime
import sys
import ctypes
sys.path.append("./")
from Methods.GetPrices import GetPrices
from Methods.Database import Database


class Ui_MainWindow(object):

    #Metodit ikkunoiden aukomiseen
    def openWindowAddItem(self):
        self.window = QtWidgets.QMainWindow()
        self.window.setFixedSize(890, 580)
        self.ui = Ui_AddItem()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle("Add Item")
        self.window.show()

    #Metodit ikkunoiden aukomiseen
    def openWindowAddShopForItem(self):
        self.window = QtWidgets.QMainWindow()
        self.window.setFixedSize(890, 580)
        self.ui = Ui_AddShopForItem()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle("Add Shop for Item")
        self.window.show()

    #Metodit ikkunoiden aukomiseen
    def openWindowOverview(self):
        self.window = QtWidgets.QMainWindow()
        self.window.setFixedSize(1056, 800)
        self.ui = Ui_Overview()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle("Overview")
        self.window.show()

    #Käyttöliittymän setuppaus
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 580)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 901, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(315, 420, 250, 150))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        self.btnAddItem = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddItem.setSizePolicy(sizePolicy)
        self.btnAddItem.setMinimumSize(QtCore.QSize(200, 200))
        self.btnAddItem.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btnAddItem.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.btnAddItem, 0, 0, 1, 1)
        sizePolicy.setHeightForWidth(self.btnAddItem.sizePolicy().hasHeightForWidth())

        self.btnAddShop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddShop.setMinimumSize(QtCore.QSize(0, 200))
        self.btnAddShop.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btnAddShop.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.btnAddShop, 0, 2, 1, 1)

        self.btnOverview = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnOverview.setMinimumSize(QtCore.QSize(0, 200))
        self.btnOverview.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btnOverview.setObjectName("pushButton")
        self.gridLayout.addWidget(self.btnOverview, 0, 4, 1, 1)

        self.btnRefresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnRefresh.setMinimumSize(QtCore.QSize(250, 50))
        self.btnRefresh.setMaximumSize(QtCore.QSize(250,50))
        self.btnRefresh.setStyleSheet('background: PaleGreen')
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnRefresh.setMinimumSize(QtCore.QSize(250,50))
        self.verticalLayout_2.addWidget(self.btnRefresh)

        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setMaximumSize(QtCore.QSize(250,50))
        self.btnExit.setStyleSheet('background: #E74C3C')
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout_2.addWidget(self.btnExit)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnRefresh.clicked.connect(self.refreshPrices)
        self.btnAddItem.clicked.connect(self.openWindowAddItem)
        self.btnAddShop.clicked.connect(self.openWindowAddShopForItem)
        self.btnOverview.clicked.connect(self.openWindowOverview)
        self.btnExit.clicked.connect(sys.exit)

    #Metodi ilmoitusikkunoiden tekoon
    def Mbox(self, title, text, style):
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    #Metodi tietokannan päivittämiseen
    def refreshPrices(self):
        try:
            databaseObject = Database
            getPricesObject = GetPrices

            items = databaseObject.getAllItems()
            links = []
            IDs = []
            newPrices = []
            date = datetime.today().strftime('%Y-%m-%d')
        
            for item in items:
                IDs.append(item[0])
                links.append(item[1])
            
            for link in links:
                if(link.startswith("https://www.jimms.fi/")):
                    try:
                        price = getPricesObject.getJimmsPrice(link)
                        price = ''.join(price.split())
                        newPrices.append(price)
                    except:
                        self.Mbox("Error", "Item not found: " + link, 0)

                elif(link.startswith("https://www.verkkokauppa.com/")):
                    try:
                        price = getPricesObject.getVerkkokauppaComPrice(link)
                        price = ''.join(price.split())
                        newPrices.append(price)
                    except:
                        self.Mbox("Error", "Item not found: " + link, 0)
                
                elif (link.startswith("https://www.prisma.fi/")):
                    try:
                        price = getPricesObject.getPrismaPrice(link)
                        price = ''.join(price.split())
                        newPrices.append(price)
                    except:
                        self.Mbox("Error", "Item not found: " + link, 0)
                elif (link.startswith("https://www.karkkainen.com/")):
                    try:
                        price = getPricesObject.getKarkkainenPrice(link)
                        price = ''.join(price.split())
                        newPrices.append(price)
                    except:
                        self.Mbox("Error", "Item not found: " + link, 0)


            databaseObject.refreshPrices(databaseObject, newPrices, date, IDs)
            self.Mbox("!", "Prices refreshed.", 0)
        
        except:
            self.Mbox("Error", "Database error", 0)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAddShop.setText(_translate("MainWindow", "Add a new shop for existing product"))
        self.btnAddItem.setText(_translate("MainWindow", "Add a new item"))
        self.btnOverview.setText(_translate("MainWindow", "Overview"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh prices"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(890, 580)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Main Menu")
    MainWindow.show()
    sys.exit(app.exec_())