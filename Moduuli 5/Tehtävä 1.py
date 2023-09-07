import random
number = 0  # Käyttäjän haluamien noppien määrä
i = 0  # Iteraattori (iterator)
dice_sum = 0  # noppien silmälukujen summa
random_dice = 0  # tallettaa satunnaisen silmäluvun nopan heitosta
number = int(input("Kuinka monta noppaa haluat heittää? "))
for i in range(0, number):
    random_dice = random.randint(1, 6)
    dice_sum = dice_sum+random_dice
print(f"Heitit ({number}) noppaa, joiden silmälukujen summa on {dice_sum}")
