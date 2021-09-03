import subprocess

interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ip a " + interface + " down", shell=True)
subprocess.call("ip a " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ip a " + interface + " up", shell=True)

subprocess.call(["ip a", interface, "down"])