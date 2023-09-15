#  Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan
#  tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi
#  21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
#  jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään
#  käyttäjältä ohjelman suorituksen alussa.
import random
tahkot = 0
dice = 0
def dice_throw():
    dice_num = random.randint(1,tahkot)
    return dice_num

tahkot = int(input("Kuinka monta tahkoa on nopassasi, heitetään sitä maksimiarvoon asti: "))
while dice != tahkot:
    dice = dice_throw()
    print(dice)
print("Heitimme maksimiarvon!")
