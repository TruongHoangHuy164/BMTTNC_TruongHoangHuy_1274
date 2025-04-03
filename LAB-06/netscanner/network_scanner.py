import requests
from scapy.all import ARP, Ether, srp

def local_network_scan(ip_range):
    print(f"Scanning IP range: {ip_range}")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        print(f"Found device: IP={received.psrc}, MAC={received.hwsrc}")
        devices.append({
            'ip': received.psrc, 
            'mac': received.hwsrc,
            'vendor': get_vendor_by_mac(received.hwsrc)
        })
    return devices

def get_vendor_by_mac(mac):
    try:
        print(f"Looking up vendor for MAC: {mac}")
        response = requests.get(f'https://api.macvendors.com/{mac}')
        if response.status_code == 200:
            return response.text
        else:
            return 'Unknown'
    except Exception as e:
        print(f'Error: {e}')
        return 'Unknown'
    
def main():
    ip_range = "192.168.1.6/24" #đổi theo ip của mình
    devices = local_network_scan(ip_range)
    for device in devices:
        print(f'IP: {device["ip"]}\tMAC: {device["mac"]}\tVendor: {device["vendor"]}')
        
if __name__ == "__main__":
    main()