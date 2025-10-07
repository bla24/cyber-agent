import scapy.all as scapy
from collections import defaultdict
import time

class PortScanDetector:
    def __init__(self, logger, notifier, action_callback=None):
        self.logger = logger
        self.notifier = notifier
        self.action_callback = action_callback
        self.syn_packets = defaultdict(list)  # {ip: [timestamps]}
        self.threshold = 10      # Nombre de ports différents en X secondes
        self.time_window = 10    # Seuil de temps en secondes

    def start(self):
        scapy.sniff(filter="tcp", prn=self._process_packet, store=0)

    def _process_packet(self, packet):
        if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.IP):
            if packet[scapy.TCP].flags == "S":  # SYN
                src_ip = packet[scapy.IP].src
                dst_port = packet[scapy.TCP].dport
                now = time.time()
                self.syn_packets[src_ip].append((dst_port, now))

                # Nettoyage des vieux paquets
                self.syn_packets[src_ip] = [
                    (port, t) for port, t in self.syn_packets[src_ip] if now - t < self.time_window
                ]
                ports_scanned = set(port for port, t in self.syn_packets[src_ip])

                if len(ports_scanned) >= self.threshold:
                    self._handle_scan(src_ip, ports_scanned)

    def _handle_scan(self, src_ip, ports):
        msg = f"Scan de port détecté depuis {src_ip} sur les ports {sorted(list(ports))}"
        self.logger.warning(msg)
        self.notifier.send_alert(msg)
        if self.action_callback:
            self.action_callback(src_ip)
        # On vide la liste pour cette IP pour éviter les alertes multiples immédiates
        self.syn_packets[src_ip] = []
