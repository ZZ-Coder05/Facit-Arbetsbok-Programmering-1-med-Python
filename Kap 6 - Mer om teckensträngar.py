""" Uppgift 1 """

# a.

def uppg1a():
    
    nabil = "Nabil"

    i = 0

    while i < len(nabil):

        print(nabil[i], end = " ")
        i += 1
    print() # Gör ny rad


    for j in nabil:

        print(j, end = "*")
    print() # Gör ny rad


    if 'Nab' in nabil:
        
        print("Nab finns i Nabil")


# b.

def uppg1b():
    
    namn = "Nabil"
    kopia = len(namn)*namn
    print(kopia)

# c.

def uppg1c():
    
    nabil = "Nabil"
    Na = nabil[0:2]
    bil = nabil[2:]
    print(Na + " " + bil)

# d. (sista uppgiften på uppgift 1)

def uppg1d():
    
    nabil = "  Nabil Merhi  "
    print(nabil.center(25, "*"))
    print(nabil.count("i", 0, 2))
    print(nabil.rjust(25, "*"))
    print(nabil.ljust(25, "'"))
    print(nabil.upper())
    print(nabil.lower())
    print(nabil.capitalize())
    print(nabil.title())
    print(nabil.strip())
    print(nabil.replace("Merhi", "Nabil"))

    print(nabil[::-1])


# Uppgift 2

def uppg2():
    inp = input("Skriv något: ")
    print("Det du har skrivit har {} tecken".format(len(inp)))

# Uppgift 3

def uppg3():
    
    forn = input("Ange förnamn: ")
    eftn = input("Ange efternamn: ")

    print(str(forn + " " + eftn).title())

# Uppgift 4

def uppg4():
    
    inp = input("Skriv något: ")
    print(inp[::-1])

# Uppgift 5

def uppg5():
    
    string = "Alla känner apan, men apan känner ingen"
    print(string.replace("apan", "gorillan"))

# Uppgift 6
def uppg6():
    
    inp1 = input("Skriv något: ")
    inp2 = input("Ange tecken du vill räkna förekomsten av: ")
    print(inp1.count(inp2))

# Uppgift 7
def uppg7():

    print("Tal", end = "")
    print("Kvadrat".rjust(10), end = "")
    print("Kub".rjust(6))

    for i in range(1, 21):

        print(i, end = "")
        print(str(i**2).rjust(8), end = "")
        print(str(i**3).rjust(9))
        
# Uppgift 8
def uppg8():
    for i in range(15):

        print((2*i*str("*") + "*").center(29))
    for i in range(13, -1, -1):

        print((2*i*str("*") + "*").center(29))


# Uppgift 9

def uppg9():
    
    inp = input("Skriv något: ").lower()
    cap = 0
    vokaler = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]

    for i in inp:

        for j in vokaler:

            if i == j:
                
                vow = i.capitalize() if cap == 0 else i
                cap = 1 if vow.isupper() else cap
                print(vow, end = "")
                break
        else:
            
            con = i.capitalize() if cap == 0 else i
            cap = 1 if con.isupper() else cap
            print(con, end = "o" + i.lower())
        
def uppg10():
    
    inp = input("Skriv något: ").lower()
    vokaler = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    res = ""
    i = 0

    while i < len(inp):
        
        for j in vokaler:

            if inp[i:i+1] == j:

                res += inp[i:i+1]
                break
        else:

            if inp[i:i+1] == inp[i+2:i+3] and inp[i+1:i+2] == "o":

                res += inp[i:i+1]
                i += 2
            else:
                
                print("Error")
        i += 1
    print(res)

        

def uppg11():
    inp = int(input("Skriv personnummer: "))
    pn = str(inp)
    pn2 = ""
    ctrl = 0
    val = 0
    j = 0

    if len(pn) < 10 or len(pn) > 11:

        print("Error")
    elif len(pn) == 11:

        pn2 = pn[0:6] + pn[7:11]
        print(pn2)
    else:
        pn2 = pn
    print("Längden på personnummret är", len(pn2))


    for i in pn2:

        if j == 0:
            
            ctrl = int(i)*2
            if ctrl > 9:
                
                ctrl -= 9
            val += ctrl
            j = 1
            
        elif j == 1:
            val += int(i)
            j = 0
            
    if val%10 != 0:
        
        print("Error")
    else:
        
        print("Godkänd")

def uppg12():

    inp = input("Hej, hur mår du? ").lower()

    g = True if inp.count("bra") or inp.count("fint") or inp.count("utmärkt") else False
    b = True if inp.count("illa") or inp.count("dåligt") or inp.count("uselt") or inp.count("inte") else False

    if g:
        
        print("Det var roligt att höra")
    elif b:

        print("Det var tråkigt")
    else:

        print("Okej")
    
