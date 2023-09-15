#  Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
#  silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan
#  kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
dice = 0
def dice_throw():
    dice_num = random.randint(1,6)
    return dice_num

while dice != 6:
    dice = dice_throw()
    print(dice)
print("Gongrats, you threw a six!")



