import socket


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

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.connect((broadcast, 0))
            sock.send(packet)

            sock.close()
