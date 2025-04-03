from scapy.all import *

def modify_icmp_packet(packet):
    if packet.haslayer(ICMP):
        
        print("ICMP Packet Info:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Type: {packet[ICMP].type}")
        print(f"Code: {packet[ICMP].code}")
        print(f"ID: {packet[ICMP].id}")
        print(f"Sequence: {packet[ICMP].seq}")
        print(f"Load: {packet[ICMP].load}")
        
        new_load = b"This is a modified ICMP packet"
        new_packet = IP(src=packet[IP].dst, dst=packet[IP].src)/ICMP(type=packet[ICMP].type, code=packet[ICMP].code, id=packet[ICMP].id, seq=packet[ICMP].seq)/new_load
        print("Modified ICMP Packet Info:")
        print(f"Source IP: {new_packet[IP].src}")
        print(f"Destination IP: {new_packet[IP].dst}")
        print(f"Type: {new_packet[ICMP].type}")
        print(f"Code: {new_packet[ICMP].code}")
        print(f"ID: {new_packet[ICMP].id}")
        print(f"Sequence: {new_packet[ICMP].seq}")
        print(f"Load: {new_packet[ICMP].load}")
        print("="*30)
        
        send(new_packet)
        
def main():
    sniff(prn=modify_icmp_packet, filter="icmp", store=0)
    
if __name__ == "__main__":
    main()