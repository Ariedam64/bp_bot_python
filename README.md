<p align="center">
  <img src="https://img.shields.io/badge/BombParty-Bot%20V2-brightgreen" alt="BombParty Bot V2" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="License MIT" />
</p>

# 💣 BombParty Bot V2

**BombParty Bot V2** est une application **Python** avec interface graphique **CustomTkinter** pour automatiser la saisie et l’interaction sur **BombParty** (jklm.fun).

<div align="center">
  <img src="https://i.imgur.com/ey1zUWa.png" alt="Aperçu de l'interface" width="600" />
</div>

---

## ⚙️ Caractéristiques

- 🔢 **Multi-bots** : Lance jusqu’à 12 bots simultanément.  
- 🎮 **Modes de jeu** :  
  - **Humain** : Typage simulé avec erreurs aléatoires.  
  - **Instant** : Réponse ultra-rapide.  
- 🤝 **Aide aux autres** : Suggestions de mots selon la syllabe.  
- 🎂 **Anniversaire** & 💥 **Suicide** : Messages automatiques.  
- 🤖 **Chat AI** : Intégration OpenAI avec personnalités (sarcastique, enfant, gentleman, oknn…).  
- 🖥️ **GUI personnalisable** : Choix du dictionnaire, clé API, nombre de bots, room, nickname.  
- 💬 **Macro-Commandes** via chat pour piloter les bots.  

---

## 📦 Installation

```bash
# Récupérer le code
git clone https://github.com/Ariedam64/bp_bot_python.git
cd bp_bot_python

# Créer et activer un environnement virtuel
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Installer les dépendances
pip install websocket-client requests customtkinter openai

# 🚀 Optionnel : Création d’un exécutable
pip install pyinstaller
pyinstaller --onefile main.py
```

---

## 🛠️ Configuration

Au premier lancement, un fichier `config.txt` est généré dans `%LOCALAPPDATA%/config.txt` (Windows) :

```text
nickname:        # Pseudonyme des bots
dic:             # Chemin vers le dictionnaire (.txt)
api_key:         # Clé API OpenAI
version: V1
```

1. **nickname** : Nom par défaut pour les bots.  
2. **dic** : Fichier de mots (1 mot/ligne).  
3. **api_key** : Clé OpenAI pour le chat AI.  

> **💡 Astuce** : Vous pouvez aussi configurer le dictionnaire et la clé via l’interface.

---

## ▶️ Utilisation

```bash
python main.py
```

1. **Room** : Code de la room (ex. `ABCD`).  
2. **Nickname** : Nom des bots.  
3. **Nombre de bots** : Curseur (1–12).  
4. **Rejoindre** / **Déconnecter**.  
5. Sélectionnez un bot pour voir son chat et configurer :  
   - **Autojoin**  
   - **Humain/Instant**  
   - **Anniversaire**, **Suicide**, **AI**, **Aide**, **$ Commandes**  
6. Envoyez un message pour que le bot y réponde.

---

## ✏️ Commandes Chat

| Commande                  | Description                                              |
|---------------------------|----------------------------------------------------------|
| `$join` / `$leave`        | Rejoindre / quitter manuellement le round                |
| `$ps human` / `$ps instant` | Mode de saisie (Humain / Instant)                  |
| `$birthday on` / `off`    | Souhaiter anniversaire                                   |
| `$suicid on` / `off`      | Mode suicide 💥                                          |
| `$ai on` / `off`          | Chat AI (OpenAI)                                         |
| `$help on` / `off`        | Aide automatique aux autres joueurs                      |
| `$humor <type>`           | Change l’humeur (sarcastique, enfant, gentleman, oknn)   |
| `$get humor`              | Affiche l’humeur actuelle                                |

---

## 📈 Dictionnaire

- Fichier `.txt` avec **1 mot par ligne**.  
- Le bot apprend automatiquement les nouveaux mots des joueurs et les ajoute.

---

## 📄 Licence

Ce projet est sous licence **MIT**.

> *Amusez-vous bien et bon jeu ! 🐤*
