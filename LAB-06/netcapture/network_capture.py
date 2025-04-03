import subprocess
from scapy.all import *

def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) > 4]
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("captured packet: ")
        print(str(packet))

interface = get_interfaces()

print("Danh sách các interface: ")
for i, iface in enumerate(interface, start=1):
    print(f"{i}. {iface}")

choice = int(input("Chọn interface: "))
selected_iface = interface[choice - 1]

# Print the list of interfaces detected by Scapy
print("Interfaces detected by Scapy:")
scapy_interfaces = get_if_list()
for i, iface in enumerate(scapy_interfaces, start=1):
    print(f"{i}. {iface}")

# Ensure the selected interface is valid for Scapy
if selected_iface not in scapy_interfaces:
    print(f"Interface '{selected_iface}' not found by Scapy. Please select a valid interface.")
else:
    sniff(iface=selected_iface, prn=packet_handler, filter="tcp")