# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa
# saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
# sort-metodille argumentiksi reverse=True
numbers = []
number_str = ""  # stores the user input as a string
number = 0  # the string will convert to a float in this variable
i = 0  # iterator that keeps count in for-loop (Have fun finding that)

number_str = input("Provide a number or end the process with a blank line: ")
if number_str != "":
    number = int(number_str)
    numbers.append(number)
while number_str != "":
    number_str = input("Provide a number of end the process with a blank answer: ")
    if number_str == "":
        break
    number = int(number_str)
    numbers.append(number)
if not numbers:
    print("You did not enter any numbers.")
else:
    numbers.sort(reverse=True)
    print("The five highest numbers provided: ")
    print(f"{numbers[:5]}")
