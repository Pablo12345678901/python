# FONCTIONS DE TRANSFORMATIONS

def transform(self, x, y):
    #return self.transform_2D(x, y) # DEBUG : pour débugguer le jeux, c'est plus facile en 2D
    # donc on laisse volontairement la fonction 2D qui ne fait aucune transformation à disposition
    return self.transform_perspective(x, y)


def transform_2D(self, x, y):  # ne fait rien, juste au cas où pour débugguer
    return int(x), int(y)  # valeur entière pour éviter les problèmes de visibilité générés par les nombres à virgules


def transform_perspective(self, x, y):
    lin_y = self.perspective_point_y * (
                y / self.height)  # proportionnellement à la distance entre y et le haut de la fenêtre
    if lin_y > self.perspective_point_y:  # éviter d'aller au-delà du point de perspective
        lin_y = self.perspective_point_y
    diff_x = x - self.perspective_point_x  # calcul de l'écart entre x et le milieu de la fenêtre
    diff_y = self.perspective_point_y - lin_y  # écart entre le nouvel y et le point de perspective - toujours > 0 pour réduire le pourcentage d'écart de x ci-dessous à mesure qu'on se rapproche du point de perspective
    factor_y = diff_y / self.perspective_point_y  # rapport en pourcentage de la différence par rapport au total
    factor_y = pow(factor_y, 4)  # mise au carré / modifier la puissance pour accentuer le phénomène
    tr_x = self.perspective_point_x + diff_x * factor_y  # départ du milieu et ajout de la différence multiplié par le ratio
    tr_y = self.perspective_point_y - factor_y * self.perspective_point_y  # en partant du haut
    return int(tr_x), int(
        tr_y)  # valeur entière pour éviter les problèmes de visibilité générés par les nombres à virgules
