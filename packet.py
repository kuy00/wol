import socket
import struct


class Packet:
    @staticmethod
    def send(ip, mac):
        mac = mac.split(':')
        address = struct.pack(
            'BBBBBB',
            int(mac[0], 16),
            int(mac[1], 16),
            int(mac[2], 16),
            int(mac[3], 16),
            int(mac[4], 16),
            int(mac[5], 16),
        )

        magic = b"\xFF" * 6 + address * 16

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic, (ip, 9))

        sock.close()
