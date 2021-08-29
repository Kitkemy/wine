wine_count = 0
children_count = 0
adult_count = 0
passenger_count = 0
while passenger_count < 20:
    print("Podaj wiek pasazera: ")
    age = int(input())
    if age == 0:
        break
    elif age < 18:
        children_count =+ 1
    else:
        adult_count += 1
    passenger_count += 1
    print("Podaj liczbę lampek wina: ")
    wine_current = int(input())
    if wine_current > 3:
        print("Nieprawidlowa liczba lampek wina")
    elif wine_current < 0:
        print("Nieprawidlowa liczba lampek wina")
    else:
        wine_count += wine_current
print("Dorosłych: {}, Dzieci: {}, lampek wina: {}, Przychód: {}".format(
    adult_count,
    children_count,
    wine_count,
    adult_count * 400 + children_count * 200 + wine_count * 10
))