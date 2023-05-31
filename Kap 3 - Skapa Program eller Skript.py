""" Uppifterna är skrivna i funktioner
    Funktionerna heter uppgift1 till uppgift8"""

# Uppgift 1

def twoNumInfo(n1, n2):
    
    numSum = n1 + n2
    numProd = n1 * n2
    info = print("The numbers you chose were {} and {}. The sum of these to numbers are {}, and the product of these two number are {}".format(n1, n2, numSum, numProd))
    return info

def uppgift1():

    num1 = int(input("Write an integer: "))
    num2 = int(input("Write another one: "))
    return twoNumInfo(num1, num2)


# Uppgift 2

def triangleAreaCalc(base, height):
    area = base * height / 2
    return print("The area of the triangle is {}".format(area))

def uppgift2():
    
    b = float(input("Input the base of the triangle: "))
    h = float(input("Input the height of the triangel: "))
    return triangleAreaCalc(b, h)


# Uppgift 3

def uppgift3():
    
    origPrice = float(input("What is the original price? "))
    print("Okay, with a 15% discount, the price would be {}".format(origPrice * 0.85))


# Uppgift 4

def discountCalc(num, procent):
    disc = num * (1-(procent / 100))
    return print("The discounted price would be {}".format(disc))

def uppgift4():
    
    price = float(input("Name another price: "))
    discount = float(input("Name the discount percentage: "))
    return discountCalc(price, discount)


# Uppgift 5

def gasReceipt(v, ppl):
    
    toPay = v * ppl
    return print("""
+-------------------------+
|         Kvitto          |
|  Tankad volym: {:>6s}kr |
| Pris per liter: {:>5s}kr |
| Betalt kronor: {:>6s}kr |
|                         |
|   Tack för besöket och  |
|   välkommen åter        |
+-------------------------+""".format(str(v), str(ppl), str(toPay)))

def uppgift5():
    
    volume = int(input("Input integer value of volume gas: "))
    pricePerLiter = int(input("Input integer value of the price per liter: "))
    return gasReceipt(volume, pricePerLiter)


# Uppgift 6

nr1 = 27
nr2 = 8
nr3 = 213

def uppgift6():
    
    return print("""
    {:>5s}
    {:>5s}
    +{:>4s}
    =====
    {:>5s}
    """.format(str(nr1), str(nr2), str(nr3), str(nr1 + nr2 + nr3)))


# Uppgift 7

float1 = 27
float2 = 8
float3 = 213

def uppgift7():
    
    return print("""
    {:>8.2f}
    {:>8.2f}
    +{:>7.2f}
    ========
    {:>8.2f}
    """.format(float1, float2, float3, float1 + float2 + float3))


# Uppgift 8

def bmiCalc(w, h):

    return w/h**2

def uppgift8():

    weight = float(input("Input your weight in kg: "))
    height = float(input("Input your height in m: "))
    bmi = bmiCalc(weight, height)
    return print("{:.1f}".format(bmi))
    
