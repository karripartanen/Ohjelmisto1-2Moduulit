#  Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#  Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten
#  pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
int_sum = 0
def int_list_sum(list):
    int_sum = sum(list)
    return int_sum

int_numbers = [2,3,14,27,32,43]
print(f"Lista kokonaisluvuista: {int_numbers}")
print(f"Kokonaislukujen summa: {int_list_sum(int_numbers)}")
