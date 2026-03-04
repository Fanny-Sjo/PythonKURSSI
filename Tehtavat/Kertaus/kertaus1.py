nimi = input("Anna nimesi: ")
hinta = 5.90
if nimi != "Matti":
      keittoannos = int(input("Montako keittoannosta?: "))
      kokonaishinta = keittoannos * hinta
      print("kokonaishinta on: ", kokonaishinta, "euroa")
      print("Seuraava, kiitos!")
else:
    print("Seuraava, kiitos!")
