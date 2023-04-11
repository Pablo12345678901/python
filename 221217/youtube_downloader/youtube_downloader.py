import pytube
import inspect
import ffmpeg
import os
import shutil
from pathlib import Path
from pytube import YouTube

def on_download_progress(stream,chunck,bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = round(bytes_downloaded * 100 / stream.filesize, 2)
    print(f"Progression du téléchargement {percent}%")


def get_url_video_from_user(URL_DE_BASE="https://www.youtube.com/") -> str:
    while True:
        url = input("Quelle est l'url de la vidéo ? ")
        if url[:len(URL_DE_BASE)] == URL_DE_BASE:
            print("L'url de la vidéo est :", url)
            return url
        print("Erreur : Veuillez saisir une url Youtube valide.")


def video_stream_itag_from_user(streams : list) -> int:
    print("AFFICHAGE DES STREAMS")
    for i in range(len(streams)):
        print(i+1, "-", streams[i].resolution)
    num_stream_max = len(streams)
    print("CHOIX DU STREAM")
    while True:
        numero_du_stream_choisi_str = input(f"Quel stream choisissez-vous ? Tapez un nombre entre 1 et {num_stream_max}. ")
        try:
            numero_du_stream_choisi_int = int(numero_du_stream_choisi_str)
            if 1 <= numero_du_stream_choisi_int <= num_stream_max:
                itag = streams[numero_du_stream_choisi_int-1].itag
                return itag
            print(f"Erreur : Veuillez saisir un nombre inclus entre 1 et {num_stream_max}. ")
        except:
            print("Erreur : Ceci n'est pas un nombre.")


def download_video(url,i):
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)
    streams_videos = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by("resolution").desc()
    best_stream_videos = streams_videos[0]
    print("Téléchargement vidéo", i)
    best_stream_videos.download("video")
    print("OK")
    print()
    streams_audio = youtube_video.streams.filter(progressive=False, type="audio").order_by("abr").desc()
    best_stream_audio = streams_audio[0]
    print("Téléchargement audio", i)
    best_stream_audio.download("audio")
    print("OK")
    print()
    audio_filename = os.path.join("audio", best_stream_audio.default_filename)
    video_filename = os.path.join("video", best_stream_videos.default_filename)
    stream_audio = ffmpeg.input(audio_filename)
    stream_video = ffmpeg.input(video_filename)
    print("Combinaison des fichiers", i)
    ffmpeg.output(stream_audio, stream_video, best_stream_videos.default_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
    print("OK")
    print()
    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
    directory_name = "dossier_final"
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    shutil.move(os.path.join(os.getcwd(), best_stream_videos.default_filename), os.path.join(os.getcwd(),directory_name))



"""  
#URL_DE_BASE = "https://www.youtube.com/"

#url = "https://www.youtube.com/watch?v=qJxk1leG1wY"
#url = get_url_video_from_user(URL_DE_BASE)

#FONCTION DEMANDER URL VIDEO

#youtube_video = YouTube(url)

print("TITRE : ", youtube_video.title)
print("NB VUES :", youtube_video.views)

#print("STREAM")
#print()

streams = youtube_video.streams
for stream in streams:
    print(stream)
print(50*"=")



# FILTRAGE DES STREAMS
#OBTENIR LES STREAMS VIDEOS UNIQUEMENT AVEC FILTRE + TYPE = "VIDEO"
streams_videos = youtube_video.streams.filter(progressive=False, file_extension='mp4', type = "video")
# TRI DE L'ORDRE DE STREAM PAR RESOLUTION DECROISSANTE
streams_videos = streams_videos.order_by("resolution").desc()
# AFFICHAGE DES STREAMS

for stream in streams_videos:
    print(stream)
    print()

# SELECTION DU MEILLEUR STREAM A L'INDEX 0
best_stream_videos = streams_videos[0]
#ENREGISTREMENT DU FICHIER VIDEO DANS UN REPERTOIRE SPECIFIQUE / CREATION SI NON EXISTANT
best_stream_videos.download("video")
# sinon, lors du téléchargement du fichier video (même nom)
# et donc l'audio écrase et remplace la vidéo

#OBTENIR LES STREAMS AUDIO UNIQUEMENT AVEC FILTRE + TYPE = "AUDIO"
streams_audio = youtube_video.streams.filter(progressive=False, type = "audio")
# TRI DE L'ORDRE DE STREAM PAR ABR (QUALITE) DECROISSANTE
streams_audio = streams_audio.order_by("abr").desc()

# AFFICHAGE DES STREAMS
for stream in streams_audio:
    print(stream)
    print()

# SELECTION DU MEILLEUR STREAM A L'INDEX 0
best_stream_audio = streams_audio[0]
#ENREGISTREMENT DU FICHIER VIDEO DANS UN REPERTOIRE SPECIFIQUE / CREATION SI NON EXISTANT
best_stream_audio.download("audio")

# itag = video_stream_itag_from_user(streams)
#stream = streams.get_highest_resolution()
#print(stream.itag)
#stream = streams.get_by_itag(140)
youtube_video.register_on_progress_callback(on_download_progress)

print("Téléchargement")
#stream.download()
print("OK")
print()

#COMBINER L'AUDIO ET LA VIDEO POUR FORMER UNE VIDEO AVEC SON SUR BASE DE 2 FICHIERS EXISTANTS
# si progressive = false, besoin de télécharger un flux vidéo + un flux audio + de les combiner
#COMPOSITION DES NOMS DE FICHIERS
audio_filename = os.path.join("audio",best_stream_audio.default_filename)
video_filename = os.path.join("video",best_stream_videos.default_filename)
#ANNONCE DES STREAMS A FFMPEG SELON LEUR PATH
stream_audio = ffmpeg.input(audio_filename)
stream_video = ffmpeg.input(video_filename)
#COMBINAISON DES FICHIERS
print("Combinaison des fichiers")
ffmpeg.output(stream_audio,stream_video, best_stream_videos.default_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
# optionneL : loglevel = évite que la description de la nouvelle vidéo s'affiche à l'écran
# optionnel : overwrite_output=True > permet d'éviter que la console demande si on doit écraser le fichier existant avec le même nom
# overwrite_output écrasera le fichier par défaut et remplacera
print("OK")
"""