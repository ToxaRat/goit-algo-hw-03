# Четверте завдання Модуль 3
from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
    # створюемо список
    users_dict = list()
    # поточна дата
    now = datetime.today().date()
    # Пройдіться по списку users та аналізуйте дати народження кожного користувача
    for user in users:
        date_user = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # міняемо год на поточний
        date_user = date_user.replace(year=now.year)
        # Розрахунок кількості днів
        days_since = date_user.toordinal() - now.toordinal()
        # на тиждне?
        if days_since>=0 and days_since<=7:
            # яка доба
            iday = int(date_user.weekday())
            if iday==5:
                date_user = date_user + timedelta(days=2) # Додаємо 2 днів
            elif iday==6:
                date_user = date_user + timedelta(days=1) # Додаємо 2 днів
            # нова дата ДН    
            sdate = date_user.strftime("%Y.%m.%d")
            user["birthday"] = sdate
            # оновити словник
            users_dict.append(user)
    return users_dict

users = [
    {"name": "Ane Smita", "birthday": "1990.01.12"},
    {"name": "John Doe", "birthday": "1985.02.08"},
    {"name": "Jane Smith", "birthday": "1990.02.10"},
    {"name": "Dane Mith", "birthday": "1990.02.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
