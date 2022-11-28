active = 1
while active:
    x = input("What would you like to do?(numeric input)")
    try:
        x = int(x)
    except:
        print("Error: enter integer input")
        continue
    if x == 1:
        pass
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 100:
        active = 0
        print("exiting menu")
    else:
        print("Error: invalid input")
