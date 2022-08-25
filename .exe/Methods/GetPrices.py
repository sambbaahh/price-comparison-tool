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


#     def getTeliaPrice(url):
#         headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
#         result = requests.get(url, headers=headers)
#         doc = BeautifulSoup(result.text, "html.parser")
#         price = doc.find('span', {'class' : 'price-now pricingText--md'})


#         print(doc)

# olio = GetPrices
# olio.getTeliaPrice("https://elisa.fi/kauppa/tuote/samsung-z-fold4-slim-standing-cover?deviceVariant=Z%20Fold4%20Slim%20Standing%20Cover%20Black&paymentOption=1")
