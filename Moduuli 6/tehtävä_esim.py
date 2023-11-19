#  Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#  Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
#  jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def list_result(nums):
    print("Nollataan kaikki listan alkiot")
    print(nums)
    nums = nums.copy()
    for i in range(5):
        nums[i] = 0
    return nums

numbers = [1, 2, 4, 7, 9]
print(list_reset(numbers))
print(numbers)  #  myös alk.per lista on muuttunut, koska
# funktiolle on syötetty parametrina viittaus siihen

def numbers_to_tuple(*nums):
    for num in nums:
        print(num)
    return nums

print(numbers_to_tuple(5, 6, 7, 22, 33))

#  monikko, eli tuple on kuin lista jota ei voi muokata
numbers = (4, 7, 9, 4)
print(numbers[2])
