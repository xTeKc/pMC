import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ip a", interface, "down"])
    subprocess.call(["ip a", interface, "hw", "ether", new_mac])
    subprocess.call(["ip a", interface, "up"])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

change_mac()