import subprocess

interface = "enp0"

subprocess.call("ifconfig enp0 down", shell=True)
subprocess.call("ifconfig enp0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig enp0 up", shell=True)
