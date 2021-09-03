import subprocess

interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ip a enp0 down", shell=True)
subprocess.call("ip a enp0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ip a enp0 up", shell=True)
