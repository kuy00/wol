import socket
import struct


class Packet:
    @staticmethod
    def send(broadcast, mac):
        if len(mac) == 17:
            sep = mac[2]
            mac = mac.replace(sep, "")
        elif len(mac) == 14:
            sep = mac[4]
            mac = mac.replace(sep, "")

        if len(mac) != 12:
            raise ValueError("Incorrect MAC address format")
        packet = bytes.fromhex("F" * 12 + mac * 16)

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.connect((broadcast, 9))
            sock.send(packet)

            sock.close()
