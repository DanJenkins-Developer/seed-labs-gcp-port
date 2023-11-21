

while True:

    print("Options: ")
    print("1. ICMP Redirect Attack Lab")

    try:
        option = int(input("Choose a lab by number: "))
        if option < 1 or option > 4:
            raise ValueError
    except ValueError:
        print("Invalid option")
        continue
    else:
        break
