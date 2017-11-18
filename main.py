""" Vigenere Cipher """
from CypherTable import CypherTable
from time import sleep

def main():
	keyWord = ""
	table = CypherTable()
	while(True):
		sleep(0.2)
		choice = menuChoice()
		
		if choice == 0:
			exit()
		elif choice == 1:
			keyWord = changeKeyWord()
		elif (choice == 2 or choice == 3) and keyWord == "" :
			print("You have to set a keyword first")
		else:
			if choice == 2:
				phrase = raw_input("Insert the phrase to enrypt: ")
				encryptedString = table.encrypt(phrase, keyWord)
				print("Original phrase: " + phrase)
				print("Encrypted phrase: " + encryptedString)
			elif choice == 3:
				phrase = raw_input("Insert the phrase to decrypt: ")
				decryptedString = table.decrypt(phrase, keyWord)
				print("Encrypted phrase: " + encryptedString)
				print("Decrypted phrase: " + decryptedString)
				

def menuChoice():
	while(True):
		""" Menu printing """
		print("  \n*** Vigenere Cipher ***")
		print("Select a voice from the menu")
		print("	1 - Insert/change key word")
		print("	2 - Encrypt the message")
		print("	3 - Decrypt the message")
		print("	0 - Quit")

		""" User input """
		try:
			choice = int(raw_input())	# converting input to integer
		except(ValueError):				
			choice = -1					# catching = -1 if not integer

		""" Selecting return value """
		if(switch(choice) == -1):
			print("*** ERROR ***")
			print("You didn't insert a correct value")
			print("Please insert it again\n")
		else:
			return switch(choice)

def switch(value):
	if value == 1:
		return 1
	elif value == 2:
		return 2
	elif value == 3:
		return 3
	elif value == 0:
		return 0
	else:
		return -1

def changeKeyWord():
	keyWord = raw_input("Choose a keyword: ").replace(" ","").lower()
	return keyWord


if __name__ == "__main__": main()