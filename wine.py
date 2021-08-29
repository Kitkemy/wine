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
        passenger_count += 1
        continue
    print("Podaj liczbę lampek wina: ")
    wine_current = int(input())
    if wine_current > 3 or wine_current < 0:
        print("Nieprawidlowa liczba lampek wina")
        continue
    wine_count += wine_current
    adult_count += 1
print("Dorosłych: {}, Dzieci: {}, lampek wina: {}, Przychód: {}".format(
    adult_count,
    children_count,
    wine_count,
    adult_count * 400 + children_count * 200 + wine_count * 10
))