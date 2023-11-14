# Flash Siklik
FLash Siklik est un jeu multijoueur inspiré de Tron utilisant les serveurs Pytactx.

## 🎯 Contexte & cahier des charges
Développé dans le cadre d'une formation, pour un formateur pour monter en compétence en Python ...

## 🎲 Règles du jeu
![](./res/maquette.png)
*Maquette du jeu*

Chaque joueur contrôle une moto laissant une trainé de couleur formant un mur derrière elle.
Un joueur est eliminé lorsqu'il percute un mur. Une partie dure X minute(s).
Un joueur peut gagner de différente manière :
- Le joueur est le dernier en vie
- Le joueur a le plus d'elimination a la fin de la partie
- Le joueur est le dernier en vie dans la phase mort subite
Une phase mort subite est déclanchée si plusieurs joueurs ayant le même nombre d'éliminations sont encore en vie à la fin de la partie.

## 🎮 Use cases
**En tant qu'administrateur je peux :**
Expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants 

<a href="./src/api/README.md#useCases"><b>En tant que joueur je peux</b></a>

## 🖧 Architecture matériel 
(optionnel, peut être décrit avec le diagramme de séquence) 
Schéma overview présentant les machines et protocoles (serveurs, clients, broker) avec texte expliquant le choix des technologies 

## 📞 Diagramme de séquence
Expliquer les points suivants
- [ ] les acteurs
- [ ] le déroulé d'une partie en partant des use case
- [ ] les données échangées entre chaque couche
- [ ] les algorithmes
- [ ] les machines
- [ ] les protocoles réseaux

## ✅ Pré-requis 
- pour l'administrateur
Matériel et logiciel requis pour executer votre projet
- pour les apprenants 
Rediriger vers README API

## ⚙️ Installation
Step by step : commandes à executer par l'administrateur, paquets à installer ...

## 🧪 Tests
- définition du plan de test ce qu'on attend quand on fait quoi 
- step by step pour lancer les tests

## 🛣️ Roadmap
Ce qui reste à faire priorisé dans le temps

## 🧑‍💻 Auteur(s)
Rendre à César ce qui appartient à César !
N'oublier pas de citer toutes les personnes qui ont contribué directement (vous) ou indirectement (les auteurs des dépendances de votre projet, des ressources récupérées ou générées ...)

## ⚖️ License
S'appuyer sur https://choosealicense.com/ ou la doc de github
Attention à vérifier la compatibilité de votre licence avec celles des modules utilisés