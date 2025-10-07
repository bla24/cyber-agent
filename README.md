# Documentation utilisateur – Agent de détection de scan de port

## Présentation

Cet agent surveille le trafic réseau pour détecter en temps réel les tentatives de scan de ports. En cas de détection, il :
- Logue l’événement dans un fichier texte
- Peut envoyer une alerte par email
- Peut exécuter (optionnellement) des actions automatiques (ex : blocage de l’IP source)
- Permet de visualiser les événements en direct via une interface web

---

## 1. Installation

### Prérequis
- Python 3.7 ou supérieur
- Accès administrateur (pour l’écoute réseau et le blocage IP)
- Accès Internet (pour l’envoi d’emails)

### Dépendances

Dans le dossier du projet :
```bash
pip install -r requirements.txt
```

---

## 2. Configuration

Modifiez le fichier `config.py` :
- **Serveur SMTP, login, mot de passe, adresses email** (pour l’alerte mail)
- **AUTO_BLOCK** : Active/désactive le blocage automatique d’IP
- **LOG_FILE** : Nom du fichier de log

---

## 3. Lancement de l’agent

Lancer l’agent avec les droits administrateur :
```bash
sudo python agent.py
```

L’agent fonctionne tant qu’il n’est pas arrêté (Ctrl+C pour stopper).

---

## 4. Visualisation en direct

Un tableau de bord web permet de suivre les alertes en temps réel.

### Lancement de l’interface web

Dans un autre terminal :
```bash
python webapp.py
```

Ouvrez ensuite votre navigateur à l’adresse :
[http://localhost:5000](http://localhost:5000)

---

## 5. Personnalisation

- **Seuil de détection** : Modifiez `threshold` et `time_window` dans `detector.py`
- **Actions automatiques** : Ajoutez ou adaptez dans `actions.py`
- **Notifications** : Ajoutez Slack, SMS, etc. via de nouveaux modules
- **Interface web** : Personnalisez `templates/index.html`

---

## 6. Précautions & conseils

- Testez d’abord en environnement isolé
- Les actions automatiques nécessitent souvent les droits root
- Ne laissez pas l’interface web accessible publiquement sans protection
- L’agent ne remplace pas une veille active ni une solution SIEM complète

---

## 7. Exemple d’utilisation courante

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votreuser/cybersec-agent.git
   cd cybersec-agent
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez `config.py` selon vos besoins
4. Lancez l’agent :
   ```bash
   sudo python agent.py
   ```
5. (Optionnel) Lancez l’interface web :
   ```bash
   python webapp.py
   ```
6. Surveillez les alertes dans le fichier de log, par email et via l’interface web

---

## Support

Pour toute question, ouvrez une issue sur le dépôt GitHub ou contactez l’auteur.
