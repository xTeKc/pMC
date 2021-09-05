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

def get_current_mac(interface):
    ip_a_result = subprocess.check_output(["ip a", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ip_a_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address")

options = get_args()
current_mac = get_current_mac(options.interface)
print(f"Current MAC = {current_mac}")
#change_mac(options.interface, options.new_mac)