import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    return = parser.parse_args()

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for  {interface} to {new_mac}")
    subprocess.call(["ip a", interface, "down"])
    subprocess.call(["ip a", interface, "hw", "ether", new_mac])
    subprocess.call(["ip a", interface, "up"])

(options, arguments) = get_args()
change_mac(options.interface, options.new_mac)