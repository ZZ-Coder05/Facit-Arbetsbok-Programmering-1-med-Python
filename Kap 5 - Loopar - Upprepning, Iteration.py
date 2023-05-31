# Uppgift 1

def uppgift1():

    print("1-15")
    for i in range(1,16):
        
        print(i)

    print("20-30")
    for j in range(20, 31):

        print(j)

    print("10--10")
    
    for k in range(10, -11, -1):

        print(k)

# Uppgift 2

def uppgift2():
    
    for i in range(100, 0, -1):
        
        print(i)
        
# Uppgift 3

def uppgift3():

    # Frågan säger ALLA udda tal mindre än 20
    # Det står inte mellan 20 och 0
    # Därför så ska negativa talen också med
    # Inte mitt fel att frågan är dåligt formulerad
    k = 20
    for i in iter(int, 1):
        
        if k % 2 == 1:
            
            print(k)
        k -= 1

# Uppgift 4

def uppgift4():
    
    j = 20
    for i in range(10):

        while 1:

            if j % 2 == 1:

                print(j)
            j -=1

# Uppgift 5

def uppgfit5():
    i = 0
    for j in range(1,51):

        i += j
    print(i)

# Uppgift 6

def uppgift6():
    print("Skriver ut XYYYY tre gånger")

# Uppgift 7

def uppgift7():
    print(20)

# Uppgift 8

def uppgift8():
    print(110)

# Uppgift 9

def uppgift9():
    
    num = 20
    squ = 0
    cub = 0
    print("{:^24s}".format("Tabell"))
    print("========================")
    print("{:>8s}{:>8s}{:>8s}".format("x", "x^2", "x^3"))

    while 1:

        # Här igen så skriver inte frågan 0 till 20, utan alla tal under 20
        # Därför kan jag bara iterera alla tal under 20, inklusive negativa tal
        squ = num**2
        cub = num**3
        print("{:>8d}{:>8d}{:>8d}".format(num, squ, cub))
        num -= 1

# Uppgift 10

def uppgift10():
    
    print("{:^24s}".format("Tabell - Temperatur"))
    print("========================")
    print("{:>12s}{:>12s}".format("Celsius", "Fahrenheit"))

    for i in range(40, -41, -1):

        print("{:>12d}{:>10.1f}".format(i, 32 + i * 9/5))

# Uppgift 11

def uppgift11():
    
    print("{:^24s}".format("Tabell - Temperatur"))
    print("========================")
    print("{:>12s}{:>12s}".format("Celsius", "Fahrenheit"))

    i = 40
    while i >= -40:

        print("{:>12d}{:>10.1f}".format(i, 32 + i * 9/5))
        i -= 1

# Uppgift 12

def uppgift12():
    
    val = 1
    interest = 0.02
    for i in range (1,2018):
        
        val += val * interest

    print(val
)
# Uppgift 13

def uppgift13():
    
    inp = input("Skriv in ett ord eller en mening: ")

    for i in inp:
        print(i)

# Uppgift 14

def uppgift14():

    psw = input("Ange lösenord / Tryck enter för att avbryta: ")

    while psw != "asf14x":
        
        if psw == "":
        
            print("Avbryter")
            break
        
        print("Felaktigt lösenord. Försök igen!")
        psw = input("Ange lösenord eller avbryt: ")
            

    else:

        print('Lösen ok!')

# Uppgift 15

def uppgift15():
    
    for i in range(9):

        print(i + 1, end=" ")

# Uppgift 16

def uppgift16():

    for i in range(5):
        
        for j in range(9):
            
            print(j + 1, end=" ")
        print("")
        
# Uppgift 17

def uppgift17():
    
    for i in range(7):

        for j in range(i):
            
            print("*", end="")
        print()
        
# Uppgift 18

def uppgift18():
    
    for i in range(10):
        
        for j in range(10):

            print(i, end=" ")
        print()
    
# Uppgift 19

def uppgift19():

    for i in range(10, 0, -1):

        for k in range(10 - i):
            
            print("  ", end="")
        for j in range(i):
        
            print(j, end=" ")
            
        print()
        
# Uppgift 20

def uppgift20():

    for i in range(1, 10):

        for j in range(1, 10):
            print("{:>4d}".format(j * i), end="")
        print()

# Uppgift 21

def uppgift21():
    
    t1 = int(input("Ange första talet: "))
    t2 = int(input("Ange andra talet: "))

    if t1 > t2:
        temp = t2
        t2 = t1
        t1 = temp

    print(t1, end=" ")
    while t1 != t2:

        t1 += 1
        print(t1, end=" ")

# Uppgift 22

def uppgift22():
    
    print("**********\n**********\n**********\n**********")
