import random


# Uppgift 1 och 2
def find(list_to_search, n):

    print(list_to_search)
    has_found = False

    for i in range(len(list_to_search)):
        if list_to_search[i] == n:
            print("Found", n, "at index", i)
            has_found = True
            break

    print("No results" if not has_found else "")


# Uppgift 3
def uppg3():
    tal = random.randint(1, 100)
    gissat_fel = True
    antal_fel = 0

    while gissat_fel:
        inp = int(input("Gissa talet: "))
        if inp == tal:
            gissat_fel = False
            print("Rätt gissat på", antal_fel)
        elif inp < tal:
            print("För lågt")
            antal_fel += 1
        else:
            print("För högt")
            antal_fel += 1


# Uppgift 4
"""Ja, det är faktiskt log bas 2 av listans storlek. I detta fallet är fallet med 100, ungefär 6.64 vilket är då 7. 
Det intressanta är alltså att det är en logaritmisk kurva"""


# Uppgift 5
def uppg5(number_list, num, low, high):

    if high >= low:
        mid = (high + low) // 2

        if num == number_list[mid]:
            return print("Found", num, "at index", mid)

        elif num < number_list[mid]:
            uppg5(number_list, num, low, mid - 1)
        else:
            uppg5(number_list, num, mid + 1, high)
    else:
        print("Did not find", num)



def uppg6():
    range = (input("What range is your number in? (separate interval with space) "))
    range_list = range.split()
    stop = False
    while not stop:
        mid = (int(range_list[1]) - int(range_list[0])) // 2 + int(range_list[0])
        q1 = input("Is your number more than, less than or equal to {}?".format(mid))
        match q1.lower():
            case "more":
                range_list[0] = mid
            case "less":
                range_list[1] = mid
            case "equal":
                print("I guessed correctly then :)")
                stop = True


def main():
    list20 = [random.randint(1, 100) for _ in range(20)]
    #find(list20, 21)

    numbers = [3, 7, 14, 19, 21, 40, 47, 47, 69, 72, 83, 87, 94, 101]
    #uppg5(numbers, 1, 0, len(numbers) - 1)
    #uppg6()


main()
