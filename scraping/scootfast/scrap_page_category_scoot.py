import requests
from bs4 import BeautifulSoup

def scrap_list_product_scoot(url):
    '''
    Entrée : Url d'une page catégorie de piece maxiscoot
    Variable modifier : Aucune 
    Sortie : Liste de dictionaire avec product_name(str), product_manufacturer(str), product_price(str), product_in_stock(boolean)
    '''
    lastest_page=False
    y=0
    list_product=[]
    while not(lastest_page):
        
        url_use=url+"?p="+str(y)+"&product_list_limit=90"
        print(url_use)

        response = requests.get(url_use)

        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')
            article = soup.find_all('li', class_='item product product-item')

            for i in range(len(article)):

                product_manufacturer =article[i].find('a')['title']
                product_name=article[i].find('a',class_='product-item-link').text.strip()
                print(article[i].find('span',class_='price').text.replace(",", ".")[0:-2].replace(" ", ""))
                product_price=float(article[i].find('span',class_='price').text.replace(",", ".")[0:-2].replace("\u202f", ""))
                product_in_stock=article[i].find('div',class_='product-availability-in-stock')
                if product_in_stock=='None':
                    product_in_stock=False
                else: 
                    product_in_stock=True
                product_link=article[i].find('a',class_='product-item-link')['href']

                list_product.append({"product_manufacturer":product_manufacturer,"product_name":product_name,"product_price":product_price,"product_in_stock":product_in_stock,"product_link":product_link})

            if soup.find('li', class_='item pages-item-next') == None:
                lastest_page=True
            else :
                y+=1
    return list_product



            
    

