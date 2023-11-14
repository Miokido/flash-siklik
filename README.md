# Flash Siklik
FLash Siklik est un jeu multijoueur inspiré de Tron utilisant les serveurs Pytactx.

![](./res/flash.png)

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
<b>En tant qu'administrateur je peux :</b>
<ul>
    <li>Decider de qui a accès au serveur</li>
    <li>Modifier la taille de la carte</li>
    <li>Modifier en direct les caracteristiques d'un agent</li>
</ul>

<a href="./src/api/README.md#useCases"><b>En tant que joueur je peux</b></a>

## 📞 Diagramme de séquence
![](./res/diagrammeSequence.png)

<!-- Expliquer les points suivants
- [ ] les acteurs
- [ ] le déroulé d'une partie en partant des use case
- [ ] les données échangées entre chaque couche
- [ ] les algorithmes
- [ ] les machines
- [ ] les protocoles réseaux -->

## ✅ Pré-requis 
**Pour l'administrateur**
- Un ordinateur connecté à internet avec python 3.10 d'installé
- Avoir un accès à un serveur privé play.jusdeliens.com

<a href="./src/api/README.md#preRequis"><b>Pour les apprenants</b></a>


## ⚙️ Installation
Execution du script d'installation fourni sur la racine du projet.

## 🧪 Tests
- Lorsqu'un agent avance, un mur se crée derrière lui
- Lorsqu'un agent fonce dans un mur, celui-ci est eliminé

## 🛣️ Roadmap
tout.

## 👨‍💻 Auteur(s)
BELLAN Tristan, CHERUEL Baptiste, DUVAL Theo, BOUCHAUD Hugo

## ⚖️ License
Under CC BY-NC-ND 3.0 licence
https://creativecommons.org/licenses/by-nc-nd/3.0/