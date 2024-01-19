import socket
from .modules import MagicPacket

def SendMagicPacket(macs:dict):
    
    BROADCAST='255.255.255.255'
    PORT=9
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    for _mac, _device in macs.items():
        packet = MagicPacket(_mac)
        sock.sendto(packet, (BROADCAST, PORT))
        print(f"[+] Sending Magic Packet to: {_mac}", end="")
        
        if _device != "":
            print(f", Device: {_device}")
        
        else:
            print()

    sock.close()        
