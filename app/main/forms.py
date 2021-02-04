from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import User

class LoginForm(FlaskForm):
    username= StringField('E-mail', validators=[DataRequired("Completer l'email"), Email('Adresse invalide')])
    password= PasswordField('Mot de passe', validators=[DataRequired()])
    remember = BooleanField('Souvenez-vous')
    submit = SubmitField('Connexion')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError("Vous n'est pas reconnu")
        else:
            if user.statut==0:
                raise ValidationError("Vous êtes bloqué")