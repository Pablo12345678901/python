import time
import requests
from pytube import YouTube

def on_download_progress(stream,chunck,bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = round(bytes_downloaded * 100 / stream.filesize, 2)
    print(f"Progression du téléchargement {percent}%")


BASE_YOUTUBE_URL = "https://www.youtube.com/"
while True :
    url = input("Copier/coller ici l'url de la vidéo à télécharger > ")
    if url.startswith(BASE_YOUTUBE_URL):
        break
    else:
        print("Erreur : Ceci n'est pas une url de vidéo YouTube.")

youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)
# appel de la fonction à chaque fois qu'il progresse
"""
#AFFICHAGE DE TOUS LES FLUX DISPONIBLES A PARTIR DE LA VIDEO
print("STREAMS")
for stream in youtube_video.streams.fmt_streams :
    print("    ",stream)
    print()
"""

stream = youtube_video.streams.get_highest_resolution()
#youtube_video est l'objet créé auparavant à partir de YouTube(url)
print("Téléchargement")
# pour afficher que le téléchargement est en cours.
stream.download()
print("OK")
# pour afficher que le téléchargement est terminé.