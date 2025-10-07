import smtplib
from email.mime.text import MIMEText
from config import MAIL_CONFIG

class EmailNotifier:
    def send_alert(self, message):
        msg = MIMEText(message)
        msg['Subject'] = "Alerte : Port Scan détecté"
        msg['From'] = MAIL_CONFIG["from_addr"]
        msg['To'] = MAIL_CONFIG["to_addr"]

        try:
            with smtplib.SMTP(MAIL_CONFIG["smtp_server"], MAIL_CONFIG["smtp_port"]) as server:
                server.starttls()
                server.login(MAIL_CONFIG["username"], MAIL_CONFIG["password"])
                server.sendmail(MAIL_CONFIG["from_addr"], [MAIL_CONFIG["to_addr"]], msg.as_string())
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'alerte email : {e}")
