import socket
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization


class Client:
    def __init__(self):
        self.private_key, self.public_key = self.load_keys()
        self.creds = self.load_json()

        while True:
            self.run()

    def gen_keys(self):
        key_size = 2048  # Should be at least 2048

        private_key = rsa.generate_private_key(
            public_exponent=65537,  # Do not change
            key_size=key_size,
        )

        public_key = private_key.public_key()

        private_key_pass = b"Help"

        encrypted_pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(private_key_pass)
        )

        with open("client_private_key.pem", 'w') as private:
            for line in encrypted_pem_private_key.splitlines():
                private.write(f"{line.decode()}\n")

        pem_public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open("client_public_key.pem", 'w') as private:
            for line in pem_public_key.splitlines():
                private.write(f"{line.decode()}\n")

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

    def run(self):
        s = socket.socket()
        port = 12345
        s.connect(('127.0.0.1', port))

        message = input(">> ")
        encrypted_message = self.encrypt(message)
        s.send(encrypted_message)
        print(s.recv(1024))
        s.close()


Client()
