import requests
from bs4 import BeautifulSoup


  # Remplacez par l'URL de la page que vous souhaitez analyser

def get_info_product(url):
    '''
    Entrée : url d'un produit maxiscoot
    Varibale modifier : aucune
    Sortie : dictionnaire avec product_url(str),product_ref(str),product_category(str),element_artikel__img(liste d'url d'image)
    '''
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Analyser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupérer toutes les div avec une classe spécifique (par exemple, 'content')
        div = soup.find('div', class_='pvd_td pvd_75__b pvd_75__b--td')

        for any in div.find_all('tr', class_='pvd_td__row'):
            var=any.text
            if len(var)>9 and var[:9] == "Référence":
                product_ref=var[9:]
            elif len(var)>15 and var[:15]=="Type de Produit":
                product_category=var[15:]

        img=soup.find_all('img', class_='pvd_mb__img')
        list_img=[]
        for any in img:
            list_img.append(any['src'])


        return {"product_ref":product_ref,"product_category":product_category,"product_url":url,"product_image":list_img}




