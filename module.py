#coding:utf-8
def menu():
	print("\t1-Infos des vols\n")
	print("\t2-Retard concernant un vol\n")
	print("\t3-Infos des vols\n")

class vol:
	def __init__(self,nom,origine,destination,durée):
		self.nom = nom
		self.origine = origine
		self.destination = destination
		self.durée = durée
	def infos_vol(self):
		print("Nom de l'avion: {}".format(self.nom))
		print("Pays de depart: {}".format(self.origine))
		print("Pays d'arrivée: {}".format(self.destination))
		print("Durée: {}".format(self.durée))
		print("le vol {} quittera {} pour {} le 20 Aout 2021à 11h30 pour une durée de {} minutes".format(self.nom,self.origine,self.destination,self.durée))

	def retard(self,temps):
		self.durée+=temps
		print("Le vol {} à destination {} aura un retard de {} qui augmente le temps {}".format(self.nom,self.destination,temps,self.durée))

def main():

	print("--------------Vol n1------------------\n")

	v1 = vol('Aire Congo','Brazzaville','Abidjan',180)
	v1.infos_vol()

	print("--------------Vol n2------------------\n")

	v2 = vol('Ethiopian Airline','Brazzaville','chine',1080)
	v2.infos_vol()
def main2():
	v2 = vol('Ethiopian Airline','Brazzaville','chine',1080)
	v2.retard(10)
if __name__ == '__main__':
	main()
	main2()






