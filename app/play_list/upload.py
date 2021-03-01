import os
import secrets
from .. import create_app
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url




config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)



#Enregistrement du fichier pdf
def play_list_doc(media):
    #Retour 
    media_fin=None
    if media is None:
        return None
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(media.filename)
    #liste des extension
    liste_ext=['.jpg', '.png', '.gif']
    if f_ext in liste_ext:
        media_fin = random_hex + f_ext
        picture_path = os.path.join(app.root_path, 'static/publication', media_fin)
        media.save(picture_path)
    else:
        upload_result = upload(media)
        media_fin=upload_result['url']
    return media_fin

def download_media(media):
    upload_result = upload(media)
    return upload_result['url']


#Enregistrement du fichier 
def save_image_mod(form_picture, ancien):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    media_fin = random_hex + f_ext
    #Suppression de l'ancien fichier
    if ancien is not None:
        chemin_offre=os.path.join(app.root_path, 'static/publication', ancien)
        if os.path.exists(chemin_offre):
            os.remove(chemin_offre)
        else:
            pass
    #Enregitrement du nouveau fichier
    picture_path = os.path.join(app.root_path, 'static/publication', media_fin)
    form_picture.save(picture_path)
    return media_fin