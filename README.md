# cour complet sur django

##1 installation de l'environnement virtuel

ici les commende inmportant sont   
*** python3 -m venv venv *** cela est la commande pour creer l'environnement virtuel
*** source venv/bin/activate *** est la commande pour activer le EV 
*** pip freeze *** our regardder les dependance deja disponible ou deha installer
*** pip freeze > requirements.txt*** elle permet de copier tout nos bibliotheque
*** pip install django *** elle permet d'installer django 
*** django-admin startproject learndjango *** permet de creer un projet en django

 ## 2 les composants
 les composants ou applivation dans django permettent de ne pas tout melanger les taches dans un meme fichier 
 et la commande permettant de creer cela est la suivante *** python3 manage.py startapp et le nom de l'application que tu voudrais donner par exemple produits *** 
  ce dossier apres sa creation doit etre mise dans le fichier settings puis faire une premier migrations avec la commande  *** python3 manage.py migrate***   dans l'application creer il ya les fichier comme 
  ### A model.py
les models  ici dand django on utilise le model ORM pour etablir un model et par la suite apres migration elle serait automatiquement transformer pas besoin d'ecrir sur sql ici voila un avantage sur cela 
poir que le model qu'on creer puis rester dans le super admin il faut enregistrer ce model dans admin.py du meme dossier 
 ### B admin.py
 est le  fichier qui contient tout les models ainsi permettant l'enregistrement et l'afficahge dans le super admin 

