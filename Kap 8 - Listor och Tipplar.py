import random


# Uppgift 1
def uppg1():
    numbers = []
    length = int(input("How many numbers do you want to add? "))
    for i in range(length):
        n = input("Number "+str(i + 1)+": ")
        numbers.append(n)
    print(numbers)


def uppg2():
    numbers = []
    length = int(input("How many numbers do you want to add? "))
    for i in range(length):
        n = input("Number " + str(i + 1) + ": ")
        numbers.append(n)
    numbers.reverse()
    print(numbers)


def uppg3():
    numbers = []
    sum = 0
    length = int(input("How many numbers do you want to add? "))
    for i in range(length):
        n = int(input("Number " + str(i + 1) + ": "))
        numbers.append(n)
        sum += n
    avg = sum / length
    print("Sum: "+str(sum)+" | Average: "+str(avg))


def uppg4():
    input_correctly = False
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    while not input_correctly:
        month_in_num = int(input("Write the number for a month: "))
        if 0 < month_in_num <= 12:
            input_correctly = True
        else:
            print("Invalid input")

    print("Your month is "+str(months[month_in_num - 1]))


def uppg5(num_list):
    min = num_list[0]
    for i in num_list:
        if i < min:
            min = i
    print(min)


def uppg6(num_list):
    """ Bygg på uppgift 4 så att det minsta talet byter plats
        med det första, varefter listan skrivs ut som kontroll"""
    # Förstår ej frågan, antar att de menar uppgift 5
    min = num_list[0]
    for i in range(len(num_list) - 1):
        if num_list[i] < min:
            num_list[0], num_list[i] = num_list[i], num_list[0]
    print(num_list)


def uppg7(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if num_list[j] > num_list[i]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    print(num_list)


def main():
    some_list = [random.randint(0, 100) for _ in range(10)]
    uppg7(some_list)


main()
