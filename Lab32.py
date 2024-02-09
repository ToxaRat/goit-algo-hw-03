# Друге завдання Модуль 3
import random

def get_numbers_ticket(min, max, quantity):
    #  створюємр список
    numbersLot = list()
    if isinstance(min, int)==False or isinstance(max, int)==False or isinstance(quantity, int)==False:
        print(f"{min}, {max}, {quantity} - повинні бути числами!")
        return numbersLot
    elif min > max:
        print(f"Перший парамет: {min} повинно буте менш другого: {max}!")
        return numbersLot
    elif (max-min+1) < quantity:
        print(f"список унікальних чисел {quantity} для заданого діапазону ({min}–{max}) недостатній!")
        return numbersLot
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
    return numbersLot


# Перший раз
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа у діапазоні від 1 до 49:", lottery_numbers)
# Другий раз - некоректні дані
lottery_numbers = get_numbers_ticket("f", 49, 6)
print("Ваші лотерейні числа у діапазоні від 1 до 49:", lottery_numbers)
# Третий раз - некоректні дані
lottery_numbers = get_numbers_ticket(10, 4, 5)
print("Ваші лотерейні числа у діапазоні від 1 до 49:", lottery_numbers)
# І на таких (10,14,6) вхідних даних програма взагалі не працює
lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа у діапазоні від 1 до 49:", lottery_numbers)