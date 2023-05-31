import random

# Uppgift 1
def uppg1():
    lotto = random.sample(range(1, 36), 7)
    print(lotto)


# Uppgift 2 a och b
def uppg2():
    stryktipsrad = []
    for i in range(13):
        r = random.randrange(0, 4)
        if r == 0 or r == 1:
            stryktipsrad.append("1")
        elif r == 2:
            stryktipsrad.append("X")
        else:
            stryktipsrad.append("2")


    for j in range (len(stryktipsrad)):
        if stryktipsrad[j] == "1":
            print(stryktipsrad[j])
        elif stryktipsrad[j] == "X":
            print("\t", stryktipsrad[j])
        else:
            print("\t\t", stryktipsrad[j])


# Uppgift 3
def uppg3():
    list1 = []
    
    for i in range(100):
        list1.append(random.randint(1, 1000))
    print("Max", max(list1))
    print("Min", min(list1))
    print("Med", sum(list1) / len(list1))


# Uppgift 4
def uppg4():
    r = random.randint(0, 2)
    doors = [0, 0, 0]
    doors[r] = 1

    choice = random.randint(0, 2)





uppg4()

