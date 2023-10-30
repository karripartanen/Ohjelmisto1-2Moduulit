#  Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
#  Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
#  ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
#  Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja
#  akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa
#  oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
#  ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle
#  haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

class Car:
    def __init__(self, plate, top_spd, cur_spd=0, dist=0):
        self.plate = plate
        self.top_spd = top_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def values(self):  # auton arvot
        print(f"Plate: {self.plate}, top speed: {self.top_spd}km/h, "
              f"distance covered: {self.dist} km.\n")

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

        print(f"Distance covered after the drive: {self.dist}km.\n")


class electric_vehicle(Car):
    def __init__(self, plate, top_speed, kwh_capacity, cur_spd, dist):
        self.kwh_capacity = kwh_capacity
        super().__init__(plate, top_speed, cur_spd, dist)

    def print_information(self):
        super().values()
        print(f"Engine capacity: {self.kwh_capacity}kWh.\n")


class petrol_vehicle(Car):

    def __init__(self, plate, top_speed, tank_volume, cur_spd, dist):
        self.tank_volume = tank_volume
        super().__init__(plate, top_speed, cur_spd, dist)

    def print_information(self):
        super().values()
        print(f"Tank volume: {self.tank_volume} liters.\n")

cars = []
cars.append(electric_vehicle("ABC-15", 180, 52.5, 60, 0))
cars.append(petrol_vehicle("ACD-123", 165, 32.3, 80, 0))
for i in cars:
    i.print_information()
    i.proceed(3)
