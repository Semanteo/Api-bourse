from bs4 import *
import requests

class api:
    def __init__(self):
        pass            
    def all(company):
        link = "https://www.boursorama.com/cours/"+ company +"/"
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            percentages = soup.select_one('span[class="c-instrument c-instrument--variation"]').text
            nam =  soup.select_one('a[class="c-faceplate__company-link"]').text
            name = nam.replace(" ", "").replace("\n", "")
            closing_price =  soup.select_one('span[class="c-instrument c-instrument--previousclose"]').text
            open_price =  soup.select_one('span[class="c-instrument c-instrument--open"]').text
            volume =  soup.select_one('span[class="c-instrument c-instrument--totalvolume"]').text
            high =  soup.select_one('span[class="c-instrument c-instrument--high"]').text
            indicative_value =  soup.select_one('span[class="c-faceplate__indicative-value"]').text
            indicative_value = indicative_value.replace(" ", "").replace("\n", " ")
            low =  soup.select_one('span[class="c-instrument c-instrument--low"]').text
            action = soup.select_one('div[class="c-faceplate__price"]').text
            action = action.replace("  ", " ")
            return  "Nom : " + name + "\nPrix de l'action : " + action  + "\nValeur indicative : " + indicative_value + "\nDernière fermeture : " + closing_price + "\nPrix d'ouverture : " + open_price + "\nHaut : " + high + "\nBas : " + low  + "\nVariation en pourcentages : " + percentages + "\nVolume : " + volume 
        except:
            return "Error to get all of " + company 
            
    def news():
        link = 'https://www.boursorama.com/bourse/'
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            hausse = soup.select_one('div[class="c-homepage-tradingboard__palmares-rise"]').text
            hauss = hausse.replace(" ", "").replace("+", " +")
            baisse = soup.select_one('div[class="c-homepage-tradingboard__palmares-drop o-vertical-interval-top-small"]').text
            baiss = baisse.replace(" ", "").replace("-", " -")
            news = soup.select_one('ul[class="c-list-news u-relative"]').text
            new = news.replace("\n", " ").replace("     ", "\n").replace("    ", "\n")
            market = soup.select_one('ul[class="c-list-news u-relative"]').text
            marke = market.replace("\n", " ").replace("     ", "\n").replace("    ", "\n")
            direct = soup.select_one('div[class="c-news"]').text
            direc = direct.replace("\n", "").replace("  ", " ").replace("     ", "\n\n")                 
            return "\nCAC\n\nActions en forte hausse : \n" + hauss + "\n\nActions en baisse : \n" + baiss + "\n\nDernières news : \n" + new + "\n\nPoints de marchés : \n" + marke + "\n\nBourse en direct : \n\n" + direc
        except:
            return "Error to get all news"