#  Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina
#  annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin
#  yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon
#  ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
#  numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon
#  hisseillä ajelemiseksi.

class Lift():

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.cur_floor = bottom_floor

    def move_to_floor(self, floor_num):
        if floor_num > self.cur_floor:
            self.floor_up(floor_num)
        elif floor_num < self.cur_floor:
            self.floor_down(floor_num)

    def floor_up(self, floor_num):
        while self.cur_floor < floor_num:
            self.cur_floor += 1
            self.notify_user()

    def floor_down(self, floor_num):
        while self.cur_floor > floor_num:
            self.cur_floor -= 1
            self.notify_user()

    def notify_user(self):
        print(f"Current floor: {self.cur_floor}")


class Building():

    def __init__(self, bottom_floor, top_floor, lift_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.lifts = [Lift(bottom_floor, top_floor) for _ in range(lift_count)]
        #  "_" eli ei väliä kuinka monta kertaa toistorakenne ajetaan

    def control_lift(self, lift_num, floor_num):
        if lift_num >= 0 and lift_num < len(self.lifts):
            lift = self.lifts[lift_num]
            print(f"\nLift number: {lift_num}")
            lift.move_to_floor(floor_num)

building = Building(1, 9, 4)

building.control_lift(1, 7)
building.control_lift(2, 4)
building.control_lift(3, 10)
