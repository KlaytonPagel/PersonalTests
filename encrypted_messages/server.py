import socket
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization


class Server:
    def __init__(self):
        self.private_key, self.public_key = self.load_keys()
        self.creds = self.load_json()

        while True:
            self.run()

    def load_keys(self) -> object:
        private_key_pass = b"Help"

        # Load a private key from a PEM file
        with open("private_key.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=private_key_pass,  # If the key is encrypted
            )

        # Load a certificate from a PEM file
        with open("public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
            )

        return private_key, public_key

    def load_json(self) -> dict:

        with open("keys.json", "r") as file:
            creds = json.loads(file.read())
        return creds

    def encrypt(self, message: str) -> bytes:
        return self.public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt(self, encrypted_message: bytes) -> str:
        try:
            message_decrypted = self.private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return message_decrypted.decode()
        except ValueError:
            return "Failed to Decrypt"

    def run(self) -> None:
        port = 12345
        s = socket.socket()
        print("Socket successfully created")

        s.bind(('', port))
        print(f"socket binded {port}")

        s.listen(5)
        print("socket is listening")

        while True:
            c, addr = s.accept()
            print('Got connection from', addr)

            encrypted = c.recv(1024)
            decrypted_message = self.decrypt(encrypted)
            if decrypted_message in self.creds.keys():
                c.send(str(self.creds[decrypted_message]).encode())
            else:
                c.send(b"False")

            c.close()
            break


Server()
