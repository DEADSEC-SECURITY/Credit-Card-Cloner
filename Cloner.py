import pickle
import os
import sys
import time
import re

def main():
	global main_input

	os.system('cls' if os.name == 'nt' else 'clear')
	print("What can i do for you:")
	print("----------------------")
	print(" 1) View already created info")
	print(" 2) Read new card")
	main_input = int(input())
	if main_input == 1:
		credit_read()
	elif main_input == 2:
		folder()
	else:
		print("Plese use only 1 or 2")
		time.sleep(1)
		main()

def folder():
	os.system('cls' if os.name == 'nt' else 'clear')
	if not os.path.exists("Credit Cards") and not os.path.exists("Other Cards"):
		os.makedirs("Credit Cards")	
		os.makedirs("Other Cards")	

		print("Creating needed files")							
		print("Please Whait")
		print("-----5-----")		
		time.sleep(1)														
		print("-----4-----")		
		time.sleep(1)														
		print("-----3-----")		
		time.sleep(1)														
		print("-----2-----")		
		time.sleep(1)														
		print("-----1-----")		
		time.sleep(1)	

		if os.path.exists("Credit Cards") and os.path.exists("Other Cards"):												
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Files created")
			clone_startUP()																														
		else:																						
			os.system('cls' if os.name == 'nt' else 'clear')
			print("If this erro continues plz create files manually")
			print("------------------------------------------------")
			print("Foulder Names:")
			print("1 - Creadit Cards")
			print("2 - Other Cards")
			sys.exit()																	
	else:	
		clone_startUP()

def clone_startUP():
	global data

	os.system('cls' if os.name == 'nt' else 'clear')
	print("Please insert a card:")
	data = input()

	if data == "":
		clone_startUP()
	else:
		clone_type()

def clone_type():
	if data[1:2] == "B":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Credit/Debit card detected")
		CreditCard()
	else:
		OtherCard()

def CreditCard():
	global regex
	global matches

	regex = r"^[^\r\nB]+B(?P<number>\d+)\^(?P<lastname>\w+)/(?P<firstname>\w+) \^(?P<firstdate>\d{2})(?P<seconddate>\d{2})\d+(?P<cvv>\d{3})0{6}\?"
	matches = re.search(regex,data)
	credit_info()

def credit_info():

	global save_input
	global fname
	global lname
	global num
	global fdate
	global sdate
	global cv

	os.system('cls' if os.name == 'nt' else 'clear')

	if matches:
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Raw Code: " + data)
		print("Card Number: " + matches.group('number'))
		print("Card Owner Name: " + matches.group('firstname') + "/" + matches.group('lastname'))
		print("Expiration Date: " + matches.group('firstdate') + "/" + matches.group('seconddate'))
		print("Security Code: " + matches.group('cvv'))
		print("---------------------------------------")
		print("Would you like to save this info? (Y/N)")
		save_input = input()

		if save_input == "Y":
			fname = matches.group("firstname")
			lname = matches.group("lastname")
			num = matches.group("number")
			fdate = matches.group("firstdate")
			sdate = matches.group("seconddate")
			cv = matches.group("cvv")
			if not os.path.exists(f"Credit Cards/{fname}-{lname}"):
				os.makedirs(f"Credit Cards/{fname}-{lname}")
				if os.path.exists(f"Credit Cards/{fname}-{lname}"):
					input_matche_number = open(f"Credit Cards/{fname}-{lname}/Card-Number","wb")
					pickle.dump(num, input_matche_number)

					input_matche_fname = open(f"Credit Cards/{fname}-{lname}/Card-First-Name","wb")
					pickle.dump(fname, input_matche_fname)

					input_matche_lname = open(f"Credit Cards/{fname}-{lname}/Card-Last-Name","wb")
					pickle.dump(lname, input_matche_lname)

					input_matche_fdate = open(f"Credit Cards/{fname}-{lname}/Card-First-Date","wb")
					pickle.dump(fdate, input_matche_fdate)

					input_matche_sdate = open(f"Credit Cards/{fname}-{lname}/Card-Second-Date","wb")
					pickle.dump(sdate, input_matche_sdate)

					input_matche_cvv = open(f"Credit Cards/{fname}-{lname}/Card-CVV","wb")
					pickle.dump(cv, input_matche_cvv)
			else:
				pass

		elif save_input == "y":
			fname = matches.group("firstname")
			lname = matches.group("lastname")
			num = matches.group("number")
			fdate = matches.group("firstdate")
			sdate = matches.group("seconddate")
			cv = matches.group("cvv")
			if not os.path.exists(f"Credit Cards/{fname}-{lname}"):
				os.makedirs(f"Credit Cards/{fname}-{lname}")
				if os.path.exists(f"Credit Cards/{fname}-{lname}"):

					input_matche_number = open(f"Credit Cards/{fname}-{lname}/Card-Number","wb")
					pickle.dump(num, input_matche_number)

					input_matche_fname = open(f"Credit Cards/{fname}-{lname}/Card-First-Name","wb")
					pickle.dump(fname, input_matche_fname)

					input_matche_lname = open(f"Credit Cards/{fname}-{lname}/Card-Last-Name","wb")
					pickle.dump(lname, input_matche_lname)

					input_matche_fdate = open(f"Credit Cards/{fname}-{lname}/Card-First-Date","wb")
					pickle.dump(fdate, input_matche_fdate)

					input_matche_sdate = open(f"Credit Cards/{fname}-{lname}/Card-Second-Date","wb")
					pickle.dump(sdate, input_matche_sdate)

					input_matche_cvv = open(f"Credit Cards/{fname}-{lname}/Card-CVV","wb")
					pickle.dump(cv, input_matche_cvv)
			else:
				pass


		elif save_input == "N":
			sys.exit()
		elif save_input == "n":
			sys.exit()
		else:
			print("Please select a valid option!")
			time.sleep(2)
			credit_info()
	else:
		sys.exit()

def credit_read():
	global read_input
	global creds_cvv
	global credit_cvv
	global creds_fname
	global credit_fname
	global creds_lname
	global credit_lname
	global creds_num
	global credit_num
	global creds_fdate
	global credit_fdate

	os.system('cls' if os.name == 'nt' else 'clear')

	print("Plese enter the name of the user: (Format type: FirstName-LastName)")
	read_input = input()

	if os.path.exists(f"Credit Cards/{read_input}"):
		with open(f"Credit Cards/{read_input}/Card-CVV", "rb") as creds_cvv:
			credit_cvv = pickle.load(creds_cvv)
		with open(f"Credit Cards/{read_input}/Card-First-Name", "rb") as creds_fname:
			credit_fname = pickle.load(creds_fname)
		with open(f"Credit Cards/{read_input}/Card-Last-Name", "rb") as creds_lname:
			credit_lname = pickle.load(creds_lname)
		with open(f"Credit Cards/{read_input}/Card-Number", "rb") as creds_num:
			credit_num = pickle.load(creds_num)
		with open(f"Credit Cards/{read_input}/Card-First-Date", "rb") as creds_fdate:
			credit_fdate = pickle.load(creds_fdate)
		with open(f"Credit Cards/{read_input}/Card-Second-Date", "rb") as creds_sdate:
			credit_sdate = pickle.load(creds_sdate)

		os.system('cls' if os.name == 'nt' else 'clear')
		print("All info that you need is here!")
		print("-------------------------------")
		print("Card Number: " + f"{credit_num}")
		print("Card Owner Name: " + f"{credit_fname}" + " | " + f"{credit_lname}")
		print("Expiration Date: " + f"{credit_fdate}" + " | " + f"{credit_sdate}")
		print("Security Code: " + f"{credit_cvv}")
		print("-------------------------------")
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Didn´t find that name if my DataBase")
		time.sleep(2)
		credit_read()

	os.system('cls' if os.name == 'nt' else 'clear')
	print("All info that you need is here!")
	print("-------------------------------")
	print("Card Number: " + f"{credit_num}")
	print("Card Owner Name: " + f"{credit_fname}" + " | " + f"{credit_lname}")
	print("Expiration Date: " + f"{credit_fdate}" + " | " + f"{credit_sdate}")
	print("Security Code: " + f"{credit_cvv}")
	print("-------------------------------")

main()