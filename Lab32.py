# Друге завдання Модуль 3
import random

def get_numbers_ticket(min, max, quantity):
    #  створюємр список
    numbersLot = list()
    # цикл 
    while True:
        # рандомне число
        target = random.randrange(min, max+1)
        # додаю у список
        numbersLot.append(target)
        # список у уникальну множину и назад
        numbersLot = list(set(numbersLot))
        # сортуемо
        numbersLot.sort()
        # кількість елементів відповидае
        if len(numbersLot) >= quantity:
            break
    return (numbersLot)


# Перший раз
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа у діапазоні від 1 до 49:", lottery_numbers)
