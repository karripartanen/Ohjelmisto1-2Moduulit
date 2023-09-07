number = 0
isPrime = True
number = int(input("Anna haluamasi luku: "))
for i in range(2, number):
    if number % i == 0:
        isPrime = False
if isPrime == True:
    print(f"Luku {number} on alkuluku.")
else:
    print(f"Luku {number} ei ole alkuluku.")

