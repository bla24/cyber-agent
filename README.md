# cyber-agent
Agent de cybersecurity automatic.

# Agent de détection de scan de port

## Fonctionnalités

- Détecte les scans de ports (SYN scan) en temps réel
- Enregistre les détections dans un fichier de logs
- Envoie un mail d'alerte
- Peut exécuter des actions automatiques (ex : blocage d'IP)

## Installation

1. Installez les dépendances Python :
   ```
   pip install -r requirements.txt
   ```

2. Modifiez `config.py` pour vos paramètres (email, logs, blocage auto).

3. Exécutez l'agent avec :
   ```
   sudo python agent.py
   ```

> **Remarque :** Les actions automatiques (blocage IP) nécessitent les droits administrateur (`sudo`).

## Extensibilité

Vous pouvez facilement :
- Ajouter d'autres méthodes de notification (SMS, Slack, etc.)
- Modifier les règles de détection
- Ajouter d'autres actions automatiques

## Attention

- Testez en environnement isolé avant toute mise en production !
- Adapter les règles de sécurité et de blocage selon votre contexte

