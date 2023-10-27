#  Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
#  tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
#  ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
#  nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
#  jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta
#  pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, plate, top_spd, cur_spd = 0, dist = 0):
        self.plate = plate
        self.top_spd = top_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def values(self):
        print(f"Plate: {self.plate}, top speed: {self.top_spd} km/h, "
              f"current speed: {self.cur_spd} km/h, distance covered {self.dist} km.")

car1 = Car("ABC-123", 142)
car1.values()







