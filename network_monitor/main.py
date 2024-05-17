from scapy.all import *


class NetworkMonitor:

    def __init__(self):
        self.packets = []
        self.start_sniffing()

        # self.create_packet()
        # self.display()

    def create_packet(self):

        for index in range(1):
            packet = send(IP(dst=f"192.168.10.{index}") / ICMP())
            if packet:
                self.packets.append(packet)

    def display(self):
        for packet in self.packets:
            packet.show()
            print(packet.sprintf("%IP.src% is active"))

    def start_sniffing(self):
        sniffer = AsyncSniffer(filter="icmp")
        sniffer.start()
        time.sleep(5)
        stuff = sniffer.stop()
        for thing in stuff:
            print(thing)

NetworkMonitor()

