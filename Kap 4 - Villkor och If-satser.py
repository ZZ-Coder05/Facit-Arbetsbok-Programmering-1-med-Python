# Uppgift 1

def uppgift1():
    
    testRes = 0
    for i in range(0,3):
        
        v = int(input("Input test result in points (0-100): "))
        testRes += v

    print(testRes/3)
    print(("", "Good job")[testRes>90])

# Uppgift 2

def uppgift2():
    
    weight = float(input("Input weight in kg: "))
    height = float(input("Input weight in m: "))
    bmi = weight/height**2

    print(bmi)
    if bmi < 18.5:
        
        print("Eat more")
        
    elif bmi >= 18.5 and bmi < 25:

        print("Just fine")
        
    elif bmi >= 25 and bmi < 30:
        
        print("Lol you getting fat")
        
    else:
        
        print("Lmao you obese")

# Uppgift 3

def uppgift3():
    
    a = 0
    b = 1
    c = 2

    if (a < b and not b < c) or (b < c and not a < b):
        
        print("Either a < b or b < c, not both")

# Uppgift 4

def uppgift4():
    inp = float(input("Input gas price per liter: "))

    # Warning, won't deal with 10, 15 or 20 kr/liter
    if inp < 10:
        
        print("That was cheap")
        
    elif inp > 10 and inp < 15:
        
        print("Refuel whole tank")
        
    elif inp > 15 and inp < 20:
        
        print("Refuel 10 liters")
        
    else:
        
        print("Now I'm selling the car and cycling instead")

# Uppgift 5

def uppgift5():

    year = int(input("Input a year: "))
    
    if year % 400 == 0:
        
        print("Leap year")
        
    elif year % 4 == 0 and not year % 100 == 0:
        
        print("Leap year")

    else:
        print("Not a leap year")
    
# Uppgift 6

def uppgift6():

    age = int(input("Input age: "))
    income = int(input("Input annual gross income: "))
    payRemark = str(input("Do you have a payment remark? Yes or No: "))

    if age < 18 and income < 120000 and payRemark == 'Yes':

        print("Get outta here, we don't wanna do business with you")

    else:

        print("Pleasure doing business with you")

# Uppgift 7

def uppgift7():
    
    if int(input("Input age: ")) < 18:

        print("Get outta here, we don't wanna do business with you")

    elif int(input("Input annual gross income: ")) < 120000:
        
        print("Get outta here, we don't wanna do business with you")
    
    elif str(input("Do you have a payment remark? Yes or No: ")) == 'Yes':

        print("Get outta here, we don't wanna do business with you")

    else:
        
        print("Pleasure doing business with you")
        
