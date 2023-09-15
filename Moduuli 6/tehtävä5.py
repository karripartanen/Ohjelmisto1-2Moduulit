#  Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#  Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina
#  saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
#  Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
#  tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
import math

def int_list(list):
    no_odds = []
    for i in list:
        if i % 2 == 0:
            no_odds.append(i)
    return no_odds


int_numbers = [2,3,12,15,43,47,58,72,73]
print(f"Original list: {int_numbers}")
print(f"List after removing odd numbers: {int_list(int_numbers)}")
