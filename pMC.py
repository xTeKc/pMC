import subprocess

interface = "enp0"
new_mac = "00:11:22:33:44:66"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig enp0 down", shell=True)
# subprocess.call("ifconfig enp0 hw ether 00:11:22:33:44:55", shell=True)
# subprocess.call("ifconfig enp0 up", shell=True)
