import mysql.connector

class Database:
    #Metodi hakee kaupat tietokannasta
    def findShops():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')
            sql_select = "SELECT shop.ShopName FROM shop"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()

            # Return array
            return records

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi lisää tavaran tietokantaan
    def addItem(self, itemName, URL, shop):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "INSERT INTO item (item.ItemName, item.URL, item.ShopID) VALUES ('" + itemName + "', " \
                + "'" + URL + \
                "', (SELECT shop.ShopID FROM shop WHERE shop.ShopName ='" + shop + "'));"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
    
    #Metodi lisää tavaran hinnan tietokantaan
    def addItemPrice(self, price, date, itemName, shop):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "INSERT INTO price (price.Price, price.Date, price.ItemID) VALUES ('" + price + "', '" + date + "'," \
                + "(SELECT item.ItemID FROM item WHERE item.ItemName = '" + itemName + \
                "' AND item.ShopID = (SELECT shop.shopID FROM shop WHERE shop.ShopName = '" + \
                shop + "')));"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee tietokannasta kaikkien tavaroiden nimet
    def getItemNames():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT item.ItemName FROM item"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records
        
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
        
    
    #Metodi hakee tietokannasta kaikki tavarat
    def getAllItems():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT item.ItemID, item.URL FROM item"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()


    #Metodi päivittää hinnat tietokannassa
    def refreshPrices(self, price, date, itemID):
        index = 0
        for item in itemID:
            try:
                connection = mysql.connector.connect(
                    host='localhost', database='PriceComparisonTool', user='root', password='admin')

                sql_select = "INSERT INTO price (price.Price, price.Date, price.ItemID) VALUES ('" + str(price[index]) + "', '" + date + "', '" + str(itemID[index]) + "');"
                cursor = connection.cursor()
                cursor.execute(sql_select)
                connection.commit()
                index += 1

            finally:
                if connection.is_connected():
                    connection.close()
                    cursor.close()

    #Metodi hakee tietokannasta kaupan tavaran nimellä
    def checkShops(item):
            try:
                connection = mysql.connector.connect(
                    host='localhost', database='PriceComparisonTool', user='root', password='admin')
                sql_select = "SELECT shop.ShopName FROM shop INNER JOIN item WHERE shop.ShopID = item.ShopID AND item.ItemName = '" + item +"'"
                cursor = connection.cursor()
                cursor.execute(sql_select)
                records = cursor.fetchall()
                return records


            finally:
                if connection.is_connected():
                    connection.close()
                    cursor.close()

    #Metodi tarkistaa että löytyykö tietokannasta samalla nimellä tavaraa
    def checkItemNames(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT "\
                "CASE WHEN EXISTS "\
                    "( "\
                        "SELECT item.ItemName FROM item "\
                        "WHERE item.ItemName = '" + itemName + "' "\
                    ") "\
                    "THEN 'TRUE' "\
                    "ELSE 'FALSE' "\
                "END"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee montako kauppaa tavaralla on
    def getShopCount(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT COUNT(shop.shopName) FROM shop INNER JOIN item ON shop.ShopID = item.ShopID WHERE item.ItemName = '" + itemName + "';"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            records = (records[0][0])
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee tavaran nykyiset hinnat
    def getCurrentPrices(itemName, limit):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT price.Price, shop.ShopName FROM price INNER JOIN item ON price.ItemID = item.ItemID" \
                " INNER JOIN shop ON item.ShopID = shop.ShopID WHERE item.ItemName = '" + itemName +  "' ORDER BY price.Date DESC LIMIT " + str(limit) + ";"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
    
    #Metodi hakee tavaran alhaisimman hinnan koskaan
    def getLowestPriceAlltime(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT MIN(price.Price), shop.ShopName FROM price INNER JOIN "\
            "item ON price.ItemID = item.ItemID INNER JOIN shop ON item.ShopID = shop.ShopID "\
            "WHERE price.Price = (SELECT MIN(price.Price) FROM price " \
            "INNER JOIN item ON price.ItemID = item.ItemID " \
            "WHERE item.ItemName = '" + itemName + "') " \
            "AND item.ItemName = '" + itemName + "';"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee tavaran korkeimman hinnan koskaan
    def getHighestPriceAlltime(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT MAX(price.Price), shop.ShopName FROM price INNER JOIN "\
            "item ON price.ItemID = item.ItemID INNER JOIN shop ON item.ShopID = shop.ShopID "\
            "WHERE price.Price = (SELECT MAX(price.Price) FROM price " \
            "INNER JOIN item ON price.ItemID = item.ItemID " \
            "WHERE item.ItemName = '" + itemName + "') " \
            "AND item.ItemName = '" + itemName + "';"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee kauppojen nimet mitkä tavaralle on lisätty
    def getShopNamesByItem(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT shop.shopName FROM shop INNER JOIN item "\
            "ON shop.ShopID = item.ShopID WHERE item.ItemName = '" + itemName + "';"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi poistaa tietokannasta tavaran hinnan
    def deleteItemPrices(self, itemName, shop):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "DELETE FROM price " \
            "WHERE price.ItemID = (SELECT item.ItemID FROM item WHERE item.itemName = '" + itemName + "' AND " \
            "item.shopID = (SELECT shop.shopID FROM shop WHERE shop.shopName = '" + shop + "'));"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi poistaa tietokannasta tavaran
    def deleteItem(self, itemName, shop):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "DELETE FROM item WHERE item.ItemName = '" + itemName + "' AND " \
            "item.ShopID = (SELECT shop.shopID FROM shop WHERE shop.shopName = '" + shop + "');"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee tietokannasta tavaran URL-osoitteen
    def getURL(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT item.URL FROM item WHERE item.ItemName = '" + itemName + "';"
            
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Hinnan haku 
    def getItemPrices(itemName,shopName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT price.Price, price.Date FROM price " \
            "WHERE price.ItemID = (SELECT item.ItemID FROM item WHERE item.itemName = '" + itemName + "' AND " \
            "item.shopID = (SELECT shop.shopID FROM shop WHERE shop.shopName = '" + shopName + "'));"
            
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()   