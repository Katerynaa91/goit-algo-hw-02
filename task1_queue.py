# Завдання 1
# Розробити програму, яка імітує приймання й обробку заявок: 
# програма має автоматично генерувати нові заявки (ідентифіковані унікальним 
# номером або іншими даними), додавати їх до черги, а потім послідовно видаляти 
# з черги для "обробки", імітуючи таким чином роботу сервісного центру.

import random
from queue import Queue


class Request:
    """Клас для генерації номерів-ідентифікаторов заявок"""

    def __init__(self):
        self.counter = random.randint(1, 999999)

    def __str__(self):
        return str(self.counter)
    
class ServiceCenter:
    """Клас для обробки заявок. Атрибут класа - об'єкт класу Queue. 
    Клас містить методи додавання елемента до черги та видалення елемента з черги. 
    Перевіряється, чи черга не порожня. Інакше, виводиться відповідне повідомлення."""

    def __init__(self):
        self.tickets = Queue()
    
    def generate_request(self, req):
        self.tickets.put(req)
        print(f"Заявка # {req} додана до черги")
    
    def process_request(self):
        if not self.tickets.empty():
            ticket_in_process = self.tickets.get()
            print(f"Заявка # {ticket_in_process} оброблена та видалена з черги")

        else: print("Немає активних заявок")


if __name__ == "__main__":

    tasks_per_day = 5
    center = ServiceCenter()

    while tasks_per_day > 0:
        task = Request()
        center.generate_request(task)
        center.process_request()
        tasks_per_day-=1
        if tasks_per_day ==0:
            print("Всі заявки оброблено. Черга пуста")
            break
            
