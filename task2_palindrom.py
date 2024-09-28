# Завдання 2
# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
# а також бути нечутливою до регістру та пробілів.

import re
from collections import deque

"""Варіант 1"""
def check_palindrom(word: str)->str|bool:
    """Функція отримує у якості параметра рядок.
    Залишаємо в рядку лише літери, інші символи видаляємо. Конвертуємо рядок в об'єкт класу deque.
    Додаємо елементи deque до іншої змінної deque справа наліво."""

    dequed_word = deque([i for i in word.lower() if i.isalpha()])
    reverse_deq = deque()

    for i in dequed_word:
        reverse_deq.appendleft(i)
    if dequed_word == reverse_deq:
        return f"The word <{word}> is a Palindrom"
    return f"The word <{word}> is not a Palindrom"

#words to check
w1 = "radar"
w2 = "r,1a  da\nr "
w3 = "symbols"
w4 = "Козак з казок"

print("-"*20)
print("Перевірка 1 варіанта")
print("-"*20)
print(check_palindrom(w1))
print(check_palindrom(w2))
print(check_palindrom(w3))
print(check_palindrom(w4))


"""Варіант 2"""

def check_palindrom2(word: str) -> str|bool:
    """Перевірка, чи є рядок паліндромом з використанням додаткових інструментів:
    - модуль re для видалення зайвих символів з рядка
    - метод .reverse() для розвертання deque-об'єкта"""

    dequed_word = deque(re.sub(r'[\W]+|[\d]+', '', word.lower()))
    w = dequed_word.copy()
    dequed_word.reverse()
    if w == dequed_word:
        return f"The word <{word}> is a Palindrom"
    return f"The word <{word}> is not a Palindrom"

print("-"*20)
print("Перевірка 2 варіанта")
print("-"*20)

print(check_palindrom2(w1))
print(check_palindrom2(w2))
print(check_palindrom2(w3))
print(check_palindrom2(w4))






