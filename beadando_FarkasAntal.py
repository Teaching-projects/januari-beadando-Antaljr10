import random

while True:
    choices = ["ko","papir","ollo"]

    computer = random.choice(choices)
    en = None

    while en not in choices:
        en = input("ko, papir, vagy ollo?: ").lower()

    if en == computer:
        print("computer: ",computer)
        print("en: ",en)
        print("Dontetlen!")

    elif en == "ko":
        if computer == "papir":
            print("computer: ", computer)
            print("en: ", en)
            print("Vesztettel!")
        if computer == "ollo":
            print("computer: ", computer)
            print("te: ", en)
            print("Nyertel!")

    elif en == "ollo":
        if computer == "ko":
            print("computer: ", computer)
            print("te: ", en)
            print("Vesztettel!")
        if computer == "papir":
            print("computer: ", computer)
            print("en: ", en)
            print("Nyertel!")

    elif en == "papir":
        if computer == "ollo":
            print("computer: ", computer)
            print("en: ", en)
            print("Vesztettel!")
        if computer == "ko":
            print("computer: ", computer)
            print("te: ", en)
            print("Nyertel!")

    ujra = input("Ujra? (igen/nem): ").lower()

    if ujra != "igen":
        break

print("viszlat!")