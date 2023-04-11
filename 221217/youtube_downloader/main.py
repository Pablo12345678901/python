import youtube_downloader
url_list = [
    "https://www.youtube.com/watch?v=BuJDaOVz2qY",
    "https://www.youtube.com/watch?v=_CL6n0FJZpk",
            ]
print("GESTION DES PATH, DOSSIER, REPERTOIRES, LOCALISATIONS".lower())
for i in range(len(url_list)):
    youtube_downloader.download_video(url_list[i],i+1)
print()
print("Téléchargement des vidéos terminé.")
