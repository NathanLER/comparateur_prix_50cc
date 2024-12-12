import requests
from bs4 import BeautifulSoup


def get_url_category_maxi(type_category):
    '''
    Entrée : une category int (1=scooter, 2=Moto 50cc, 3=Mob,4 =Moto cross)
    Variable modifier : Aucune
    Sortie : une liste des différentes catégorie
    '''



    response = requests.get("https://www.maxiscoot.com/")

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Analyser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find_all('div', class_='sb_lh__dn_item')


        type_category_scrap=div[type_category-1].find_all('a', class_='sb_dn_flyout_menu__link sb_dn_flyout_menu__link--l1 sb_dn_flyout_menu__link--has_subitems')
        liste_category=[]
        for category in type_category_scrap:
            if category['href'][-1]=="/":
                liste_category.append(category['href'])
    
    return liste_category
        


