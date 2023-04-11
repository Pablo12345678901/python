import time

from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from time import sleep



Builder.load_file("canvas_exemples.kv")

class CanvasExemple1(Widget):
    pass

class CanvasExemple2(Widget):
    pass

class CanvasExemple3(Widget):
    pass

class CanvasExemple4(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=5)
            Color(0, 1, 0, 1)
            Line(circle=(200, 200, 100))
            Line(rectangle=(100, 100, 500, 200))
            Color(1, 0, 1, 1)
            self.rect = Rectangle(pos=(300,200), size=(150, 100))

    def on_button_a_click(self):
        inc = dp(10)
        w, h = self.rect.size
        x, y = self.rect.pos
        # la différence correspond à ce qu'il reste entre
        # le bord de la fenêtre et l'extrémité droite du rectange
        # qui est équivalente à sa position (extrémité gauche) + sa largeur
        diff = self.width - (x+w)
        if diff < inc:
            # si la différence est plus petite que l'incrément
            # celui-ci sera modifié à la baisse
            inc = diff
        # ajout de l'incrément
        x += inc
        self.rect.pos = (x, y)

class CanvasExemple5(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        # ajout des vitesses x et y à __init__
        self.vx = dp(6)
        self.vy = dp(8)
        with self.canvas:
            self.ball = Ellipse(pos=(100,100), size=(self.ball_size, self.ball_size))
        # update est une fonction a créer ci-dessous
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        #DEBUG print("on size: " + str(self.width) + ", " + str(self.height))
        # la balle se positionnera au centre de l'écran avec ajustement selon sa taille
        # car self.center correspond au coin inférieur gauche de la balle
        # donc il faut la décaller vers en bas à gauche de la moitié de sa taille sur les 2 axes
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        # Gestion des incréments pour éviter de sortir de l'écran, même partiellement
        inc_x = self.vx
        inc_y = self.vy
        # récupération des valeurs initiale
        x, y = self.ball.pos
        # si la vitesse est positive ...
        if inc_x > 0:
            # la différence est égale à la largeur soustraite du coin gauche + la largeur de la balle
            diff_x = self.width - (x + self.ball_size)
        else:
            # sinon la différence est la position de x
            diff_x = x
        # idem pour y
        if inc_y > 0:
            diff_y = self.height - (y + self.ball_size)
        else:
            diff_y = y
        # si la différence est plus petite que la vitesse
        # et que celle-ci est positive
        if ((diff_x < inc_x) and (inc_x > 0)):
            # on ajuste la vitesse à la différence pour éviter le dépassement
            inc_x = diff_x
            # et on inverse la vitesse pour la prochaine ocurrence
            self.vx = -self.vx
        # si la vitesse est plus petite que l'inverse de la différence
        # et que celle-ci est négative
        # signifiant ainsi sans modification de la vitesse, l'objet sortira de l'écran
        elif (inc_x < -diff_x) and (inc_x < 0):
            # ajustement de l'incrément
            inc_x = -diff_x
            # inversement de la vitesse
            self.vx = -self.vx
        # idem pour y
        if ((diff_y < inc_y) and (inc_y > 0)):
            inc_y = diff_y
            self.vy = -self.vy
        elif (inc_y < -diff_y) and (inc_y < 0):
            inc_y = -diff_y
            self.vy = -self.vy
        # ajout des incréments
        x += inc_x
        y += inc_y
        #DEBUG print("diff_x : " + str(diff_x) + ", diff_y : " + str(diff_y))
        #DEBUG pour contrôler que l'objet ne sort jamais de l'écran
        # ajudstement de la position de l'objet après incrémentation
        self.ball.pos = (x, y)

class CanvasExemple6(Widget):
    pass

class CanvasExemple7(BoxLayout):
    pass
