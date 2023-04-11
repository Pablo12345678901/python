# FONCTION DE GESTION DES TOUCHES CLAVIER / APPUI SUR ECRAN
from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self.keyboard.unbind(on_key_down=self.on_keyboard_down)
    self.keyboard.unbind(on_key_up=self.on_keyboard_down)
    self.keyboard = None

# EN CAS D'APPUI SUR TOUCHE CLAVIER
def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left': # si la touche droite est appuyée
        self.current_speed_x = self.SPEED_X # sinon on va vers la gauche
    elif keycode[1] == 'right': # si la touche droite est appuyée
        self.current_speed_x = -self.SPEED_X # alors on va vers la droite
    return True # il faut laisser le return True

# EN CAS DE RELACHEMENT DE TOUCHE CLAVIER
def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0 # en cas de relachement du clic, la vitesse redevient 0

def on_touch_down(self, touch): # fonction qui se déclenche automatiquement en cas de clic
    #state_game_over = False  # la variable passera à True si game over
    #state_game_has_started = False  # la variable passera à True lors du lancement du jeu
    if not self.state_game_over and self.state_game_has_started: # condition qui gère les appui de touch que en jeu et hors GAME OVER
        if touch.x < self.width/2: # si le clic a eu lieu dans la moitié de gauche de l'écran
            self.current_speed_x = self.SPEED_X # alors on va vers la droite
        else:
            self.current_speed_x = -self.SPEED_X # sinon on va vers la gauche
    return super(RelativeLayout, self).on_touch_down(touch)
    # le super fait appel au parent pour éviter d'attraper le clic sur le bouton à la place
    # de la fonction "on_menu_button_pressed" du fichier main.py

def on_touch_up(self, touch): # fonction qui se déclenche automatiquement en cas de relachement de clic
    self.current_speed_x = 0 # en cas de relachement du clic, la vitesse redevient 0