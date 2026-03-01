from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n--- Packet Captured ---")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")

# Capture 10 packets
sniff(prn=packet_callback, count=10)
