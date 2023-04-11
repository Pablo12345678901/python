str = "PAS BESOIN DE CLASS POUR GERER LE IFRAME - C'EST AUTOMATIQUEMENT IFRAME"
print(str.lower())

"""

enlever les ul > transformer en p
mettre le tout ds div
bordure 1 px - couleur lightgrey
mettre du padding pr un affichage optimal
texte centré
taille 14px

"""
<ul>
    {% for pizza in pizzas % }
        <li> {{pizza.nom}}</li>
    {% endfor %}
</ul>
