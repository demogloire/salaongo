from flask import render_template, flash, url_for, redirect, request, session
from .. import db, bcrypt
from ..models import Promotion
from app.promotion.forms import AjoutPromotionForm, ModifierPromotionForm
from flask_login import login_user, current_user, logout_user, login_required
from ..utilites.utility import title_page, date_sup_ver
from . import promotion
from app.promotion.upload import save_image_mod
from app.promotion.upload import play_list_doc, download_media





@promotion.route('/', methods=['GET','POST'])
def index():
   title=title_page('Promotion')
   #Requête d'affichage de la promotion
   listes=Promotion.query.all()
   
   return render_template('promotion/index.html', title=title, liste=listes)


''' Ajout d'une promotion '''
@promotion.route('/ajout', methods=['GET','POST'])
def ajoutPromotion():
   title='Promotion | Makunywa Consulting'
   #formulaire
   
   form=AjoutPromotionForm()
   if form.validate_on_submit():
      media=form.url.data
      print(media,'----------------------------')
      verification_media = play_list_doc(media)
      if date_sup_ver(form.date_debut.data, form.date_fin.data):
         enre_promotion=Promotion(nom_promotion=form.nom_promotion.data, date_debut=form.date_debut.data, date_fin=form.date_fin.data, url=verification_media )
         db.session.add(enre_promotion)
         db.session.commit()
         flash("Ajout avec succès",'primary')
         print('Bien')
      else:
         print('Faux')


   return render_template('promotion/ajout.html',  title=title, form=form)


""" Modifier statut de l'Utilisateur """
@promotion.route('/statut/<int:promotion_id>', methods=['GET', 'POST'])
def statut(promotion_id):
   #Titre
   title=title_page('Promotion')
   #Requête de vérification de la promotion
   statut_promotion= Promotion.query.filter_by(id=promotion_id).first()

   if statut_promotion is None:
      return redirect(url_for('promotion.index'))

   if statut_promotion.statut == True:
      statut_promotion.statut=False
      db.session.commit()
      flash("La promotion est désactivée sur la plateforme",'primary')
      return redirect(url_for('promotion.index'))
   else:
      statut_promotion.statut=True
      db.session.commit()
      flash("La promotion est activée sur la plateforme",'primary')
      return redirect(url_for('promotion.index'))
   
   return render_template('user/index.html',title=title)


# """ Modification promotion  """

@promotion.route('/edit_<int:promotion_id>_cate', methods=['GET', 'POST'])
def edit(promotion_id):

   form=ModifierPromotionForm()
   #Titre
   title=title_page('Promotion')
   #Requête de vérification du type
   modif_promotion=Promotion.query.filter_by(id=promotion_id).first_or_404()
   print(modif_promotion.nom_promotion,'******************************************')

   if form.validate_on_submit():

      image_pub=save_image_mod(form.url.data, modif_promotion.url)

      if modif_promotion is not None:
         modif_promotion.nom_promotion=form.nom_promotion.data
         modif_promotion.date_debut=form.date_debut.data
         modif_promotion.date_fin=form.date_fin.data
         if image_pub is None:
            return redirect(url_for('promotion.edit', promotion_id=promotion_id))
         else:
            nouv_enreg_image= save_image_mod(form.url.data, modif_promotion.url)
         
         db.session.add(nouv_enreg_image)

      db.session.commit()
      flash("Modification réussie",'primary')
      return redirect(url_for('promotion.index'))
      
   if request.method=='GET':
      form.nom_promotion.data=modif_promotion.nom_promotion
      form.date_debut.data=modif_promotion.date_debut
      form.date_fin.data=modif_promotion.date_fin


   return render_template('promotion/edit.html', form=form, title=title, modif_promotion=modif_promotion, url_m=modif_promotion.url)

