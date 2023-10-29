#  Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen
#  numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi
#  on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun
#  h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
#  kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä
#  yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
#  Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi
#  kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
import random

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


elevator = Lift(1, 6)
elevator.move_to_floor(6)
elevator.move_to_floor(1)
