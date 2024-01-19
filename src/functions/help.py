import sys

def help():
    print("""Usage:
  wol <'MAC,device'/s> [options]
          
Example:
  - wol 00:00:00:00:00:00,test > "MAC,device"
  - wol --file /example/path/macs.json > only from file
  - wol 00:00:00:00:00:00,test 11:11:11:11:11:11 --file /example/path/macs.json > mix of all options

Options:
  --help, -h               Display this help message

File Handling Options:
  --file, -f               Read MAC addresses from a file            
                           The file should have a ".json" extension with the following structure:
                           {"MAC": "device_name", "MAC2": "device_name2", ...}

Author: m0opha.""")
    sys.exit(0)
