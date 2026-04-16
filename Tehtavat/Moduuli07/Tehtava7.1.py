vuodenajat = ("talvi", "kevät", "syksy", "talvi") #Monikko

kuukausi = int(input("Mikä kuukauden numero (1-12)? "))

vuodenaika_numero = ((kuukausi -1) % 12) // 3

print("Vuodenaika on ", vuodenajat[vuodenaika_numero])

# tai luettelee ekalle riville 3x talvi 3x kevät jne.
# sitten voi suoraan hakea kuukauden numerolla monikosta eikä tarvi tehdä laskua % 12 // 3
# kuukausi -1 kuitenkin tehtävä koska monikko alkaa nollasta