# arp_spoofing

> Simple educational ARP spoofing / forwarding examples (for local testing only).

This repository contains two small Python scripts:

- `spoof.py` — performs an ARP spoofing / poisoning attack between victims (educational use only).
- `forward.py` — a simple IPv4 forwarding helper to forward packets while spoofing is active.

Requirements
- Python 3.8+
- scapy (install with `pip install scapy`)

Usage (example)
1. Ensure you have permission to test on the target network.
2. Run the forwarder on the machine acting as the gateway (if needed):

   python forward.py

3. Run the spoof script to poison ARP caches (run as root/Administrator):

   sudo python spoof.py

Safety & Legal
- These scripts are provided for educational and testing purposes only. Do not use them on networks you do not own or have explicit permission to test.

License
- No license specified. Use responsibly.
