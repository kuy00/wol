from fastapi import FastAPI
from arp import Arp
from packet import Packet

app = FastAPI()


@app.get('/mac')
def search_mac_address(net: str):
    mac_list = Arp.search(net)
    return mac_list


@app.get('/ip')
def get_mac_by_ip(ip: str):
    mac_address = Arp.get_mac_by_ip(ip)
    return {
        'ip': ip,
        'mac': mac_address,
    }


@app.get('/send')
def send_magic_packet(broadcast: str, mac: str):
    try:
        Packet.send(broadcast, mac)
        return 'success'
    except Exception:
        return 'error'
