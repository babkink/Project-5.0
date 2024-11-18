
from queue import Queue
from threading import Thread
import time
from random import randint
from threading import Lock

class Table:
    def __init__(self, number, guest = 'None'):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        # self.daemon = True

    def run(self):
        time.sleep(randint(3,10))

class Cafe:
    q = Queue()
    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                var = False
                if table.guest == 'None':
                    table.guest = guest.name
                    guest.start()
                    print(f'Guest {guest.name} is on the table {table.number}')
                    var = True
                    break
            if not var:
                self.q.put(guest.name)
                print(f'Guest {guest.name} is in the queue')

    def serve_guests(self):
        while not self.q.empty() or all([table.guest != 'None' for table in tables]):
            for guest in guests:
                if not guest.is_alive():
                    for table in tables:
                        time.sleep(1)
                        if table.guest == guest.name:
                            table.guest = 'None'
                            print(f'Guest {guest.name} finished the meal and table number {table.number} is available')
                            if not self.q.empty():
                                guest = self.q.get()
                                table.guest = guest
                                for i in guests:
                                    if i.name == guest:
                                        i.start()
                                        break
                                print(f'Guest {i.name} came from queue and sit on the table {table.number}')
                                break
                            else:
                                break





tables = [Table(number) for number in range(1, 5)]
guest_names = ['Ana', 'Bob', 'Vova', 'Mike', 'Konsta', 'Egor', 'Max']
guests = [Guest(name) for name in guest_names]
# for guest in guests:
#     guest.start()
#     # print(threading.current_thread())
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.serve_guests()

