#  Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan
#  automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä
#  toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h
#  ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
#  Sitten kilpailu alkaa.
#  Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10
# ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
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

#  aivan kauheaa koodia

