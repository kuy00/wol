from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from arp import Arp
from packet import Packet

app = FastAPI()


@app.middleware('http')
async def check_private_ip(request: Request, call_next):
    client_host = request.client.host

    if not client_host.startswith('172') and not client_host.startswith('10')\
            and not client_host.startswith('192') and not client_host.startswith('127'):
        return PlainTextResponse("Unauthenticated")

    response = await call_next(request)
    return response


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
