===============================
BASIC NETWORK SNIFFER PROJECT
===============================

Project Title:
Basic Network Packet Sniffer using Python (Scapy)

--------------------------------
1. Project Description
--------------------------------
This project is a simple network packet sniffer built using Python and the Scapy library.
It captures network packets and displays useful information such as:

- Source IP Address
- Destination IP Address
- Protocol Type (TCP / UDP / ICMP / Other)

The program captures 10 packets and prints their details in the terminal.

--------------------------------
2. Requirements
--------------------------------
Operating System:
- Kali Linux (Recommended)
- Or any Linux system

Software:
- Python 3
- Scapy library

--------------------------------
3. Installation Steps
--------------------------------
Step 1: Update system
sudo apt update

Step 2: Install Scapy (if not already installed)
sudo apt install python3-scapy

--------------------------------
4. How to Run the Program
--------------------------------
Step 1: Save the Python file as:
sniffer.py

Step 2: Run the program using:
sudo python3 sniffer.py

(Note: Root privileges are required to capture network packets.)

--------------------------------
5. How It Works
--------------------------------
- The program uses Scapy's sniff() function to capture packets.
- It checks if the packet contains an IP layer.
- It extracts:
    • Source IP address
    • Destination IP address
- It identifies the protocol:
    • TCP
    • UDP
    • ICMP
    • Other

The program captures only 10 packets (count=10).

--------------------------------
6. Example Output
--------------------------------
--- Packet Captured ---
Source IP: 192.168.1.5
Destination IP: 142.250.183.14
Protocol: ICMP

--------------------------------
7. Learning Outcomes
--------------------------------
- Understanding how network packets flow.
- Learning basic networking protocols.
- Hands-on experience with packet capturing.
- Understanding how sniffers work.

--------------------------------
8. Important Note
--------------------------------
This program is developed strictly for educational purposes.
Use it only on authorized networks.
Unauthorized packet sniffing may be illegal.

--------------------------------
Author:
Ezaz Ahmed

Course:
Cyber Security / Network Security Lab

Date:
01 March,2026
--------------------------------
