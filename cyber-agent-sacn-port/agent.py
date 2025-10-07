from detector import PortScanDetector
from logger import setup_logger
from notifier import EmailNotifier
from actions import block_ip

def main():
    logger = setup_logger()
    notifier = EmailNotifier()
    detector = PortScanDetector(logger=logger, notifier=notifier, action_callback=block_ip)

    print("Agent de détection de scan de port démarré. Appuyez sur Ctrl+C pour arrêter.")
    try:
        detector.start()
    except KeyboardInterrupt:
        print("\nArrêt de l'agent.")

if __name__ == "__main__":
    main()
