from subprocess import Popen
from time import sleep

servers = ["185.169.134.3", "185.169.134.4", "185.169.134.43", "185.169.134.44", "185.169.134.45", "185.169.134.5", "185.169.134.59", "185.169.134.61", "185.169.134.107", "185.169.134.109", "185.169.134.166", "185.169.134.171", "185.169.134.172", "185.169.134.173", "185.169.134.174", "80.66.82.191", "80.66.82.190", "80.66.82.188", "80.66.82.168", "80.66.82.159", "80.66.82.200", "80.66.82.144", "80.66.82.132", "80.66.82.128"]

for server in servers:
    Popen(f'"RakSAMP Lite.exe" -h {server} -p 7777')
    sleep(1)
print(f"total {len(servers)} servers")