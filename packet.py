from scapy.all import scapy, sniff, Ether, sr1, IP, ICMP

import platform

print("Scapy is ready!")

val = input("How many packets do you want to capture: ")
print(f"You selected {val} packets to capture!")

packets = sniff(filter="not ip6", count=int(val))

for packet in packets:
	print(packet)

# choice = input("What ip address would you like to ping? ")
# print(f"You choose ip {choice}.")

# sr1(IP(dst=choice)/ICMP())
