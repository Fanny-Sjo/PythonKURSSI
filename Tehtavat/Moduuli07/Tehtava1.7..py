vuodenajat = ("talvi", "kevät", "syksy", "talvi") #Monikko

kuukausi = int(input("Mikä kuukauden numero (1-12)? "))

vuodenaika_numero = ((kuukausi -1) % 12) // 3

print("Vuodenaika on ", vuodenajat[vuodenaika_numero])