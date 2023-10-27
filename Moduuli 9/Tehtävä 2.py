#  Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa
#  parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen,
#  auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
#  Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
#  Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
#  sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
#  Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
#  Kuljettua matkaa ei tarvitse vielä päivittää.
class Car:
    def __init__(self, plate, top_spd, cur_spd = 0, dist = 0):
        self.plate = plate
        self.top_spd = top_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def values(self):
        print(f"Plate: {self.plate}, top speed: {self.top_spd} km/h, "
              f"current speed: {self.cur_spd} km/h, distance covered {self.dist} km.\n")

    def accelerate(self, spd_change):
        if spd_change < 0:
            self.cur_spd = self.cur_spd + spd_change
            if self.cur_spd < 0:
                self.cur_spd = 0
                print("The car emergency braked and has stopped.\n")
            elif self.cur_spd > 0:
                print(f"The car has slowed down to {self.cur_spd}km/h.\n")
        elif spd_change > 0:
            self.cur_spd = self.cur_spd + spd_change
            if self.cur_spd > self.top_spd:
                self.cur_spd = self.top_spd
                print(f"Top speed has been reached: {self.top_spd}km/h\n")
            elif self.cur_spd < self.top_spd:
                print(f"The car has accelerated to {self.cur_spd}km/h\n")


car1 = Car("ABC-123", 142)
car1.values()
for i in [30, 70, 50, -200]:
    car1.accelerate(i)

