from scapy.all import scapy, sniff, Ether
import platform

print("Scapy is ready!")

val = input("How many packets do you want to capture: ")
print(f"You selected {val} packets to capture!")

IFACE_NAME="Killer(R) Wi-Fi 6 AX1650w 160MHz Wireless Network Adapter (200D2W)"

if platform.node() == 'DESKTOP-ISJO6EN':
	packets = sniff(iface=IFACE_NAME, filter="not ip6", count=int(val))
	print("This is Jason's Computer")
else:
	packets = sniff(filter="not ip6", count=int(val))
	print("This is not Jason's Computer")

for i in packets:
	print(i.summary())
