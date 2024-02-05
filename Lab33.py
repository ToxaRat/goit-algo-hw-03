# Третє завдання Модуль 3
import re


def normalize_phone(phone_number):
    phone = phone_number
    # Видаліть всі символи, крім цифр та '+', з номера телефону
    pattern = r"[^+1234567890]"
    replacement = ""
    phone = re.sub(pattern, replacement, phone)
    # чи номер починається з '38'
    if phone.find("38")==-1:
        phone = "38"+phone
    # чи номер починається з '+'
    if phone.find("+")==-1:
        phone = "+"+phone
    return phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)