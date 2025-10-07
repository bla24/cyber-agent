# Configuration de l'agent

LOG_FILE = "portscan.log"

MAIL_CONFIG = {
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "username": "alert@example.com",
    "password": "mot_de_passe",
    "from_addr": "alert@example.com",
    "to_addr": "destinataire@example.com"
}

# Actions automatiques
AUTO_BLOCK = True  # Bloquer automatiquement les IP suspectes (si True)
