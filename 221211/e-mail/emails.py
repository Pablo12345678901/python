# CONTENU DU FICHIER DE REDACTION EMAIL
import emails_config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def envoyer_email(email_destinataire, sujet, message):
    multipart_message = MIMEMultipart()
    # création d'un objet intermédiaire
    # pour avoir du contenu diversifié : HTML, titre e-mail
    multipart_message["Subject"] = sujet
    multipart_message["From"] = emails_config.config_server
    # montre les informations de l'expéditeur sur l'e-mail reçu > possible modifier
    multipart_message["To"] = email_destinataire
    # montre les informations du destinataire sur l'e-mail reçu > possible modifier
    multipart_message.attach(MIMEText(message,"plain"))
    # 2ème paramètre = plain pour du texte en tant que message
    # 2ème paramètre = html pour de l'HTML en tant que message > utile pour mettre du style (grand, gras, ajout de table)
    serveur_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)
    # établissement d'un connexion non sécurisée (sans SSL ou TSL) au serveur
    # paramètres = serveur et port
    serveur_mail.starttls()
    # établissement d'un connexion sécurisée avec TSL
    serveur_mail.login(emails_config.config_email, emails_config.config_password)
    # login à l'adresse e-mail
    # paramètres = identifiants de connexion (e-mail et MDP)
    serveur_mail.sendmail(emails_config.config_email, email_destinataire,
                          multipart_message.as_string())
    # Envoi de l'e-mail
    # paramètres : e-mail de l'expéditeur, e-mail du destinataire
    serveur_mail.quit()
    # quit ferme la connexion

texte = """
Bonjour,
TEST"""
# écrire des e-mail à plusieurs lignes avec des retours à la ligne.
# Attention, les accents ne sont pas bien compris avec le décodeur ASCII
# Besoin trouver une combine pour envoyer des e-mails avec accents.
envoyer_email("pablo.zamora@outlook.fr", sujet="E-mail depuis Python", message=texte)