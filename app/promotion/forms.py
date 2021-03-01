from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Promotion


class AjoutPromotionForm(FlaskForm):
    nom_promotion=StringField('Nom', validators=[DataRequired("Entrer le nom de la promotion")])
    date_debut=StringField('Date de debut', validators=[DataRequired("Entrer la date de début")])
    date_fin=StringField('Date de fin', validators=[DataRequired("Entrer la date de fin")])
    url=FileField("Selectionner un fichier", validators=[FileAllowed(['mp4','png','jpg','gif','mp3'],'Seuls les fichiers png, jpg, gif, mp3 et mp4 sont autorisés')])
    submit = SubmitField('Promotion')


class ModifierPromotionForm(FlaskForm):
    nom_promotion=StringField('Nom', validators=[DataRequired("Entrer le nom de la promotion")])
    date_debut=StringField('Date de debut', validators=[DataRequired("Entrer la date de début")])
    date_fin=StringField('Date de fin', validators=[DataRequired("Entrer la date de fin")])
    url=FileField("Selectionner un fichier", validators=[FileAllowed(['mp4','png','jpg','gif','mp3'],'Seuls les fichiers png, jpg, gif, mp3 et mp4 sont autorisés')])
    submit = SubmitField('Promotion')


