from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget


class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):  # fonction qui se déclenche automatiquement en cas de clic
        if self.opacity == 0:
            # la fonction s'éxécute que si l'opacité est différente de 0
            # que si on est dans le jeu
            return False
        return super(RelativeLayout, self).on_touch_down(touch)
