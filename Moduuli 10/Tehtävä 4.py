#  Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
#  jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen
#  lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan
#  ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
# tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle
# kulje-metodia.

# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi
# muotoiltuna.

# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään
# kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen
# tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä
# kertaalleen sen jälkeen, kun kilpailu on päättynyt.
import random

class Car:
    def __init__(self, plate, top_spd, cur_spd=0, dist=0):
        self.plate = plate
        self.top_spd = top_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def values(self):  # auton arvot
        print(f"Plate: {self.plate}, top speed: {self.top_spd}km/h, "
              f"current speed: {self.cur_spd} km/h, distance covered: {self.dist} km.\n")

    def accelerate(self, spd_change):  # kiihdytä-metodi
        if spd_change < 0:
            self.cur_spd = self.cur_spd + spd_change
            if self.cur_spd < 0:
                self.cur_spd = 0
                print(f"{self.plate} emergency braked and has stopped.\n")
            elif self.cur_spd > 0:
                print(f"{self.plate} has slowed down to {self.cur_spd}km/h.\n")
        elif spd_change > 0:
            self.cur_spd = self.cur_spd + spd_change
            if self.cur_spd > self.top_spd:
                self.cur_spd = self.top_spd
                print(f"{self.plate} has reached the top speed of: {self.top_spd}km/h\n")
            elif self.cur_spd < self.top_spd:
                print(f"{self.plate} has accelerated to {self.cur_spd}km/h\n")

    def proceed(self, hour):  # kulje-metodi
        extra_dist = hour * self.cur_spd
        self.dist = self.dist + extra_dist

        print(f"Distance covered after the drive: {self.dist}")


'''
car1 = Car("ABC-123", 142, 60, 3500)  # nopeudet km/h muodossa
car1.values()

for i in [30, 70, 50, -200]:
    car1.accelerate(i)

car1.proceed(1.5)
'''
race_cars = []
for i in range(10):
    plate = (f"ABC-{i + 1}")
    top_speed = random.randint(100, 200)
    race_cars.append(Car(plate, top_speed, 0, 0))

race_winner = None
target = 10000
while not race_winner:
    for car in race_cars:
        car.accelerate(random.randint(-10, 15))
        car.proceed(1)
        if car.dist >= target:
            race_winner = car
            break

print(f"Winner of the race: {race_winner.plate}!\n")
print("Results:\n")
for car in race_cars:
    print(f"Plate: {car.plate}, top speed: {car.top_spd}km/h, distance driven: {car.dist}km.")
