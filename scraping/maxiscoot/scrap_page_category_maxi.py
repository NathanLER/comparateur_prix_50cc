import requests
from bs4 import BeautifulSoup
import re

def get_nb_page(url):
    '''
    Entrée : Url d'une page catégorie de piece maxiscoot
    Variable modifier : Aucune 
    Sortie : le nombre de page de la catégorie(int)
    '''
    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        nb=soup.find('div', class_='element_sr2__pager_y')
        if nb==None:
            return 1
        else :
            return int(nb.text)


def scrap_list_product_maxi(url):
    '''
    Entrée : Url d'une page catégorie de piece maxiscoot
    Variable modifier : Aucune 
    Sortie : Liste de dictionaire avec product_name(str), product_manufacturer(str), product_price(str), product_in_stock(boolean),product_link(str)
    '''
    list_product=[]

    for y in range(get_nb_page(url)):
        url_use=url+"?p="+str(y)
        
        response = requests.get(url_use)
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Analyser le contenu HTML avec BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Récupérer toutes les div avec une classe spécifique (par exemple, 'content')
            div = soup.find_all('a', class_='element_artikel element_artikel__clickable element_product_grid__item')

            

            for i in range(len(div)):

                product_ico = div[i].find('img', class_='element_artikel__img')['src']

                product_manufacturer= div[i].find('div', class_='element_artikel__brand').text.strip()

                product_name= div[i].find('h3', class_='element_artikel__description').text.strip()

                product_link= div[i]['href']

                product_price=float((div[i].find('div', class_=re.compile(r'element_artikel__price price')).text.strip().replace(".", "").replace(",", "."))[0:-2])

                product_in_stock = div[i].find('div', class_='element_artikel__availability').text.strip()
                if product_in_stock=='En stock':
                    product_in_stock=True
                else :
                    product_in_stock=False
                
                list_product.append({"product_manufacturer":product_manufacturer,"product_name":product_name,"product_price":product_price,"product_in_stock":product_in_stock,"product_link":product_link, "product_ico": product_ico})
    return list_product





