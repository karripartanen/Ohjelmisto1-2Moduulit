#  Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan
#  tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella
#  vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen
#  kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa
#  kuljetun matkan lukemaan 2090 km.

class Car:
    def __init__(self, plate, top_spd, cur_spd = 0, dist = 0):
        self.plate = plate
        self.top_spd = top_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def values(self):  # auton arvot
        print(f"Plate: {self.plate}, top speed: {self.top_spd} km/h, "
              f"current speed: {self.cur_spd} km/h, distance covered: {self.dist} km.\n")

    def accelerate(self, spd_change): #  kiihdytä-metodi
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

    def proceed(self, hour):  #  kulje-metodi
        extra_dist = hour * self.cur_spd
        self.dist += extra_dist
        print(f"Distance covered after the drive: {self.dist}")





car1 = Car("ABC-123", 142, 60, 1500) # nopeudet km/h muodossa
car1.values()
'''
for i in [30, 70, 50, -200]:
    car1.accelerate(i)
'''
car1.proceed(1.5)  # auto ajaa puolentoista tunnin ajan

