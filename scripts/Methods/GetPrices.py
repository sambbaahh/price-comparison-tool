from bs4 import BeautifulSoup
import requests


class GetPrices:
    #Metodi hakee Jimmsin sivuilta tavaran hinnan
    def getJimmsPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        price = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text
        price = price.replace(',', '.')
        return price
        
    #Metodi hakee Verkkokauppa.comin sivuilta tavaran hinnan
    def getVerkkokauppaComPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        data = doc.find('data',{'data-price' : 'current'})
        priceInteger = data["data-integer"]
        priceDecimal = data["data-decimals"]
        price = priceInteger + "." + priceDecimal
        return price

    #Metodi hakee Prisman sivuilta tavaran hinnan
    def getPrismaPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        price = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text
        price = price.replace(',', '.')
        return price

    #Metodi hakee Kärkkäisen sivuilta tavaran hinnan
    def getKarkkainenPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        priceInteger = doc.findAll('span', {'class' : 'euros'}, text = True)[0].text
        priceDecimal = doc.findAll('span', {'class' : 'cents'}, text = True)[0].text
        price = priceInteger + "." + priceDecimal
        return price