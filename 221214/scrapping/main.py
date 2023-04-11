from bs4 import BeautifulSoup
import requests



url = "/Users/alejandramt/Desktop/Développement/221214/scrapping/SITE_RECETTE/recette.html"
f = open(url, "r")
html_content = f.read()
soup = BeautifulSoup(html_content, 'html.parser')
f.close()


list_div_centre = soup.find_all("div", class_="centre")
paragraphe = list_div_centre[1].find("p", class_="description")
print(paragraphe.text)
print()


list_div_info = soup.find_all("div", class_="info")
if list_div_info:
    if len(list_div_info)>=2:
        for each in list_div_info:
            print(div_info.text)
    else:
        img = list_div_info[0].find("img")
    print(img["src"])
    print()