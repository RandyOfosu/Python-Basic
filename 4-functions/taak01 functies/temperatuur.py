def tempconverter(vraag1):
    if vraag1[-1] == 'c' or vraag1[-1] == 'C':
        gradencelsius = int(vraag1[:-1])
        gradenfahrenheit = gradencelsius * 9 / 5 + 32
        print('Het is', gradenfahrenheit, '°F')
    elif vraag1[-1] == 'f' or vraag1[-1] == 'F':
        gradenfahrenheit = int(vraag1[:-1])
        gradencelsius = (gradenfahrenheit - 32) * 5 / 9
        print('Het is', gradencelsius, '°C')
    else:
        print("Wat is dit?")


vraag1 = input("Hoeveel graden is het? ")


tempconverter(vraag1)