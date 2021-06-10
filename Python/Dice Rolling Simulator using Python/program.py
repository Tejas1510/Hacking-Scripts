import random
import time
x = "y"

while x == "y":

    # Gnenerates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    str = "Rolling..."
    strp = str.center(93)
    print("\n")
    print(strp)
    print("\n")
    time.sleep(0.5)
    no = random.randint(1, 6)

    if no == 1:
        print("\t\t\t\t\t __________")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|    0     |")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|__________|") 
    if no == 2:
        print("\t\t\t\t\t __________")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|        0 |")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|0         |")
        print("\t\t\t\t\t|__________|")
    if no == 3:
        print("\t\t\t\t\t __________")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|        0 |")
        print("\t\t\t\t\t|    0     |")
        print("\t\t\t\t\t|0         |")
        print("\t\t\t\t\t|__________|")
    if no == 4:
        print("\t\t\t\t\t __________")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|__________|")
    if no == 5:
        print("\t\t\t\t\t __________")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|    0     |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|__________|")
    if no == 6:
        print("\t\t\t\t\t __________")
        print("\t\t\t\t\t|          |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|0       0 |")
        print("\t\t\t\t\t|__________|")

    x = input("Press (y) to roll again and for exit press any other key: ")
    print("\n")
