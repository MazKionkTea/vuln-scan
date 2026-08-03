import help

import subprocess

nmap = subprocess.Popen("nmap")
target = input(help.target, "target : ")
teknik = input("-sS, -sT, -sU, -sF\nteknik pemindaian port: ")
port = input("spesifikasi port : ")
deteksi = input("deteksi layanan & os : ")
NSE = input()
waktu = input()
eva_spoof = input()
output = input()