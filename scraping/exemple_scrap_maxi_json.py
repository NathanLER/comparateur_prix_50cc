from maxiscoot.scrap_category_list_maxi import *
from maxiscoot.scrap_item_maxi import *
from maxiscoot.scrap_page_category_maxi import *
import json


scrap_maxi_haut_moteur_50cc =scrap_list_product_maxi('https://www.maxiscoot.com/fr/moto-50cc/haut-moteur/')


with open('maxi_50cc_haut_moteur_dump.json', 'w') as fichier_json:
    # Utiliser json.dump pour écrire la liste dans le fichier
    json.dump(scrap_maxi_haut_moteur_50cc, fichier_json, indent=4, ensure_ascii=False)
