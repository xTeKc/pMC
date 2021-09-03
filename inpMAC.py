import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

parser.parse_args()

interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ip a " + interface + " down", shell=True)
# subprocess.call("ip a " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ip a " + interface + " up", shell=True)

subprocess.call(["ip a", interface, "down"])
subprocess.call(["ip a", interface, "hw", "ether", new_mac])
subprocess.call(["ip a", interface, "up"])