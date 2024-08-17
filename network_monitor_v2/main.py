import json
from subprocess import Popen, PIPE
from re import findall
import threading
import time
from alert import EmailAlert


# a program to monitor my network and send alerts for devices that connect or disconnect________________________________
class NetworkMonitor:
    def __init__(self):
        self.addresses = {}
        self.alert = EmailAlert("example@email.com")  # place the sender email here
        self.recipient_email = "example@email.com"  # place the recipients email here

    # pull all known devices from the json file and load into memory_______________________________
    def get_addresses(self):
        with open('network_monitor.json', 'r') as file:
            self.addresses = json.load(file)

    # send a singular ping to the specified address then parse the result and handle properly______
    def send_ping(self, address):

        data = ""  # used to aggregate responses
        output = Popen(f"ping {address} -n 1", stdout=PIPE, encoding="utf-8")  # runs ping command

        # parse ping response
        for line in output.stdout:
            data = data + line
            result = findall("TTL", data)

        # if we get echo reply add device when new, reset notify countdown
        if result:
            try:
                content = self.addresses[address].split()
                # content[0] = notify countdown
                # content[1] = ip address
                # content[2] = name in notification
                # content[3] = notify flag
                self.addresses[address] = f"{4} {content[1]} {content[2]} {content[3]}"

                # If notify flag is set send a reconnected notification
                if content[0] == "-1" and content[3] == "True":
                    subject = "Device Reconnected"
                    message = f"{content[2]} {content[1]} Reconnected"
                    self.alert.send_alert(subject=subject, message=message, receiver_email=self.recipient_email)

            except KeyError:
                self.addresses[address] = f"4 {address} NewDevice True"

                # send alert for new device connecting
                subject = "New Device Connected"
                message = f"{address} Connected For The First Time"
                self.alert.send_alert(subject=subject, message=message, receiver_email=self.recipient_email)

        # if we don't get echo reply and device known drop the notify counter by one
        else:
            try:
                content = self.addresses[address].split()
                if int(content[0]) < 0:
                    content[0] = -1

                # set countdown to negative one and send disconnect alert
                elif int(content[0]) == 0 and content[3] == "True":
                    content[0] = -1
                    subject = "Device Disconnected"
                    message = f"{content[2]} {content[1]} Disconnected"
                    self.alert.send_alert(subject=subject, message=message, receiver_email=self.recipient_email)

                # drop the countdown by one
                else:
                    content[0] = int(content[0]) - 1

                # content[0] = notify countdown
                # content[1] = ip address
                # content[2] = name in notification
                # content[3] = notify flag
                self.addresses[address] = f"{content[0]} {content[1]} {content[2]} {content[3]}"
            except KeyError:
                pass

    # dump the current connection status from memory to the json file___________________________________________________
    def set_json(self):
        with open('network_monitor.json', 'w') as file:
            json.dump(self.addresses, file, indent=4)

    # Start the process loop____________________________________________________________________________________________
    def start(self):
        self.get_addresses()
        while True:
            self.set_json()
            for i in range(1, 256):  # ip range to ping
                threading.Thread(target=lambda: self.send_ping(f"192.168.1.{i}")).start()  # ping on different threads
            time.sleep(15)  # wait before pinging again


NetworkMonitor().start()
