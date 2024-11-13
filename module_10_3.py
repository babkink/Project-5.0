import threading
from random import randint
import time

lock = threading.Lock()

class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self):
        counter_deposit = 100
        while counter_deposit:
            a = randint(50, 500)
            if self.balance > 500 and lock.locked():
                lock.release()
            else:
                self.balance += a
                print(f'Account replenishment for {a}, balance is {self.balance}, give counter is {counter_deposit}')
            counter_deposit -= 1
            time.sleep(0.001)


    def take(self):
        counter_take = 100
        if self.balance > 0 and lock.locked():
            lock.release()
        while counter_take:
            a = randint(50, 500)
            print(f'request to issue {a}')
            if a <= self.balance:
                self.balance -= a
                print(f'Withdrawal from account of {a}, balance is {self.balance}, take counter is {counter_take}')
            else:
                with lock:
                    print(f'Balance is {self.balance}. Insufficient amount at account to issue {a}, take counter is {counter_take}')
            counter_take -= 1
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Final balance is {bk.balance}')