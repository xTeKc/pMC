import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for  {interface} to {new_mac}")
    subprocess.call(["ip a", interface, "down"])
    subprocess.call(["ip a", interface, "hw", "ether", new_mac])
    subprocess.call(["ip a", interface, "up"])

options = get_args()
#change_mac(options.interface, options.new_mac)

ip_a_result = subprocess.check_output(["ip a", options.interface])
print(ip_a_result)

re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ip_a_result)