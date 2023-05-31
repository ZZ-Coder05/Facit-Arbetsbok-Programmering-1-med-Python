# Uppgift 1
def isfloat(string):
    try:
        float(string)
    except:
        return False
    return True


def isint(string):
    try:
        int(string)
    except:
        return False
    return True


def main():
    print(isfloat("34f"))
    print(isint("32"))

main()
