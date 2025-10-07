from config import AUTO_BLOCK
import subprocess

def block_ip(ip):
    if AUTO_BLOCK:
        try:
            # Exemple Linux : bloque l'IP avec iptables
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            print(f"Action automatique : IP {ip} bloquée.")
        except Exception as e:
            print(f"Erreur lors du blocage de l'IP {ip} : {e}")
    else:
        print(f"Blocage automatique désactivé. (IP {ip} non bloquée)")
