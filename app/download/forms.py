from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Playlist


class Ajout_play_list_Form(FlaskForm):
    url=FileField("Selectionner un fichier", validators=[FileAllowed(['mp3 , mp4'],'Seuls les fichiers mp3 et mp4 sont autorisés')])
    submit = SubmitField('Playlist')

    #Fornction de verification d'unique existenace dans la base des données
    def validate_url(self, url):
        type= Playlist.query.filter_by(url=url.data).first()
        if type:
            raise ValidationError("Ce nom existe déjà")


