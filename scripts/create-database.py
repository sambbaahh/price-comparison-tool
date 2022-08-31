import mysql.connector

def createDatabase():
    try:
        connection = mysql.connector.connect(
            host='localhost', database='PriceComparisonTool', user='root', password='admin')
        sql_select = "DROP DATABASE if EXISTS PriceComparisonTool; CREATE DATABASE PriceComparisonTool; USE PriceComparisonTool; CREATE TABLE Shop ( ShopID INT AUTO_INCREMENT, ShopName VARCHAR(50) NOT NULL, PRIMARY KEY (ShopID)); CREATE TABLE Item( ItemID INT AUTO_INCREMENT,ItemName VARCHAR(100) NOT NULL,URL VARCHAR(500) NOT NULL, ShopID INT NOT NULL,PRIMARY KEY (ItemID), FOREIGN KEY (ShopID) REFERENCES Shop(ShopID));CREATE TABLE Price (PriceID INT AUTO_INCREMENT,Price DECIMAL(10,2) NOT NULL,Date DATE NOT NULL,ItemID INT NOT NULL, PRIMARY KEY (PriceID),FOREIGN KEY (ItemID) REFERENCES Item(ItemID));"
        cursor = connection.cursor()
        cursor.execute(sql_select)
        
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

def createShops():
    try:
        connection = mysql.connector.connect(
            host='localhost', database='PriceComparisonTool', user='root', password='admin')
        sql_select = "INSERT INTO shop (shop.ShopName) VALUES ('Jimms'), ('Verkkokauppa.com'), ('Prisma'), ('Karkkainen');"
        cursor = connection.cursor()
        cursor.execute(sql_select)
        connection.commit()

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

                
createDatabase()
createShops()