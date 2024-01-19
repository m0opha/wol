import os
import sys

from .modules import parser
from .help import help
from ..variables import allowed_arg

def ArgHandler():
    macs = {}
    file_paths = []

    extracted_args = parser()
    if len(extracted_args) == 2 and extracted_args["lone"] == None:
        help()

    for arg, value in extracted_args.items():
        if arg not in allowed_arg:
            print(f"[+] Unrecognized argument: {arg}")
            sys.exit(1)

        elif arg in ["--help", "-h"]:
            help()

        elif arg == "lone":
            if value is None:
                continue
            
            if isinstance(value, list):
                for _mac in value:
                    dm = _mac.split(",")
                    
                    MAC = dm[0]
                    device = ""
                    
                    if len(dm) == 2:
                        MAC = dm[0]
                        device = dm[1] 

                    if len(MAC.split(":")) != 6:
                        print(f"[-] Invalid MAC format: {_mac}")
                        sys.exit(1)


                    macs[(_mac)] = "" 
            
                continue
            
            dm = value.split(",")
            MAC = dm[0]
            device = ""

            if len(dm) == 2:
                device = dm[1] 

            if len(MAC.split(":")) != 6:
                print(f"[-] Invalid MAC format: {value}")
                sys.exit(1)

            macs[MAC]= device
        
        elif arg in ["-f", "--file"]:
            if value is None:
                print("[+] File path is required.")
                sys.exit(1)

            if isinstance(value, list):
                for path in value:
                    if os.path.isfile(path):
                        file_paths.append(os.path.abspath(path))
                    
                    else:
                        print(f"[-] File path doesn't exist: {path}")
                        sys.exit(1)
                continue

            if os.path.isfile(value):
                file_paths.append(os.path.abspath(value))

            else:
                print(f"[-] File path doesn't exist: {value}")
                sys.exit(1)

    return macs, file_paths

