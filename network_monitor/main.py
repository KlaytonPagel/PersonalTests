import time
import threading
import json
from scapy.all import *


# A class for monitoring the network and reporting whenever a device is connected or disconnected_______________________
class NetworkMonitor:

    # Set up the network monitor________________________________________________________________________________________
    def __init__(self):

        # a dictionary to hold all found addresses_________
        self.addresses = {}
        self.sniffer = None

        # Start the sniffer and run the program____________
        self.start_sniffing()
        self.run()

    # Uses multiple threads to send pings out to the entire subnet______________________________________________________
    def send_pings(self):
        print("starting pings")

        # Load all known addresses from the json file______
        self.load_json()

        # Use different threads to ping each address_______
        for index in range(256):
            threading.Thread(target=lambda: send(IP(dst=f"192.168.1.{index}") / ICMP(), verbose=0)).start()

        # wait for the pings to finish_____________________
        time.sleep(5)

    # save the devices IP and MAC address to the dictionary to be loaded into the JSON later____________________________
    def capture(self, pkt):
        data = pkt.sprintf("%Ether.src% %IP.src%").split(" ")

        ip_connection = self.addresses[data[0]].split()
        if ip_connection[1] == "-1":
            print(f"{ip_connection[0]} Reconnected")
        self.addresses[data[0]] = f"{data[1]} {3}"

    # Load all previously seen addresses into the address dictionary____________________________________________________
    def load_json(self):
        with open('network_monitor.json', 'r') as f:
            self.addresses = json.load(f)
            f.close()

    # Save the current dictionary to the JSON file______________________________________________________________________
    def save_json(self):
        with open('network_monitor.json', 'w') as f:
            json.dump(self.addresses, f, indent=4)
            f.close()

        print("Saving Addresses")

    # Start the packet sniffer only capturing ICMP replies______________________________________________________________
    def start_sniffing(self):
        self.sniffer = AsyncSniffer(filter="icmp[icmptype] != icmp-echo", prn=self.capture)
        self.sniffer.start()

    # Checks to see if the device is connected__________________________________________________________________________
    def check_connection_drop(self):

        # Loops through all devices ever connected_________
        for address in self.addresses.keys():

            # Separates the ip address and the connection__
            ip_connection = self.addresses[address].split()
            ip_connection[1] = int(ip_connection[1]) - 1

            # checks if the connection has dropped off_____
            if ip_connection[1] == 0:
                print(f"{ip_connection[0]}: Disconnected")
                self.addresses[address] = f"{ip_connection[0]} {-1}"
            elif ip_connection[1] < 0:
                pass
            else:
                self.addresses[address] = f"{ip_connection[0]} {ip_connection[1]}"

    # Continuously run the program______________________________________________________________________________________
    def run(self):

        self.send_pings()
        self.check_connection_drop()
        self.save_json()

        time.sleep(5)
        self.run()


NetworkMonitor()

