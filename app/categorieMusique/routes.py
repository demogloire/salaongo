from flask import render_template, flash, url_for, redirect, request, session
from .. import db, bcrypt
from ..models import Categorieplaylist
from app.categorieMusique.forms import AjoutCatForm
from flask_login import login_user, current_user, logout_user, login_required
from ..utilites.utility import title_page
from . import categorieMusique



''' Ajout d' une categorisation de musique '''

@categorieMusique.route('/ajouter', methods=['GET','POST'])
def ajouter():
   title='Catégorie musique | Makunywa Consulting'
   #formulaire
   form=AjoutCatMusique()
   if form.validate_on_submit():
      nom_cat=form.type_musique.data.capitalize()
      #Requete de verification de la catégorie
      categorie_enre=Categorie(type_musique=type_musique)
      db.session.add(categorie_enre)
      db.session.commit()
      flash("Ajout avec succès",'primray')
      return redirect(url_for('categorieMusique.index')) 

   return render_template('categorieMusique/ajouter.html',  title=title, form=form)

""" Liste de catégorie de musique """

@categorieMusique.route('/', methods=['GET', 'POST'])
def index():
   #Titre
   title=title_page('Catégorie musique')
   #Requête d'affichage de la categorisation
   listes=Categorieplaylist.query.order_by(Categorieplaylist.id.desc()).all()

   return render_template('categorieMusique/index.html',title=title, liste=listes)

""" Modifier statut de l'Utilisateur """
# @categorie.route('/statut/<int:cat_id>', methods=['GET', 'POST'])
# def statut(cat_id):
#    #Titre
#    title=title_page('Catégorie')
#    #Requête de vérification de la categorie
#    cat_statu=Categorie.query.filter_by(id=cat_id).first()

#    if cat_statu is None:
#       return redirect(url_for('categorie.index'))

#    if cat_statu.statut == True:
#       cat_statu.statut=False
#       db.session.commit()
#       flash("La catégorie est désactivée sur la plateforme",'primary')
#       return redirect(url_for('categorie.index'))
#    else:
#       cat_statu.statut=True
#       db.session.commit()
#       flash("La catégorie est activée sur la plateforme",'primary')
#       return redirect(url_for('categorie.index'))
   
#    return render_template('user/index.html',title=title)


# # """ Modification de la catégorie  """

# @categorie.route('/edit_<int:cate_id>_cate', methods=['GET', 'POST'])
# def edit(cate_id):

#    form=AjoutCatForm()
#    #Titre
#    title=title_page('Catégorie')
#    #Requête de vérification du type
#    cate_class=Categorie.query.filter_by(id=cate_id).first()
#    #Le nom du type encours de modification
#    cate_nom=cate_class.nom

#    if cate_class is None:
#       return redirect(url_for('categorie.index'))
   
#    if form.validate_on_submit(): 
#       cate_class.nom=form.nom.data.capitalize()
#       db.session.commit()
#       flash("Modification réussie",'primary')
#       return redirect(url_for('categorie.index'))
      
#    if request.method=='GET':
#       form.nom.data=cate_class.nom

#    return render_template('categorie/edit.html', form=form, title=title, cate_nom=cate_nom)

