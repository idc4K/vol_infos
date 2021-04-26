from module import *
import os

while True:
	menu()
	choix = int(input(">"))

	if choix == 1:
		main()
		print("\tAppuyer sur 0 pour continuer et 3 pour quitter")
		reponse = int(input(">"))
		if reponse == 3:
			break
		elif reponse == 0:
			os.system("cls")
			continue
			
			
	elif choix == 2:
		main2()
		print("\tAppuyer sur 0 pour retourner au menu ou 3 pour quitter")
		reponse = int(input(">"))
		if reponse == 3:
			break
		elif reponse == 0:
			os.system("cls")
			continue
	elif choix == 3:
		break

os.system("cls")
print("\t Merci d'avoir consulter notre application\n")