# Перше завдання Модуль 3
from datetime import datetime

def get_days_from_today(datestr):
    try:
        # Перетворіть рядок дати у форматі 'YYY-MM-ДД' у об'єкт datetime
        datetime_object = datetime.strptime(datestr, "%Y-%m-%d")
    except ValueError:
        print(f"дата не у форматі 'YYY-MM-ДД'")
        return None
    # поточна дата
    now = datetime.today()
    # Розрахунок кількості днів
    days_since = now.toordinal() - datetime_object.toordinal()
    # Поверніть різницю у днях як ціле число
    return days_since

# з приклада
razdate = get_days_from_today("2021-10-09")
print(f"Різниця у днях: {razdate}")
# попередній місяц
razdate = get_days_from_today("2024-01-31")
print(f"Різниця у днях: {razdate}")
# наступний місяц
razdate = get_days_from_today("2024-03-01")
print(f"Різниця у днях: {razdate}")
# невірний формат!!!
razdate = get_days_from_today("2024.03.01")
print(f"Різниця у днях: {razdate}")
