import socket
import sys
from .functions import ArgHandler, ReadFile, SendMagicPacket

def main():
    Total_MACs={}
    MACs = {}
    exMACs, file_paths = ArgHandler()
    
    for _path in file_paths:
        macs.update(ReadFile(_path))
    
    Total_MACs.update(exMACs)
    Total_MACs.update(MACs)
    SendMagicPacket(Total_MACs)

if __name__ == "__main__":
    main()
