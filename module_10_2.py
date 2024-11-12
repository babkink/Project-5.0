import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name
        self.enemy = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, we were attacked!')
        while self.enemy:
            self.enemy -= self.power
            self.days += 1
            time.sleep(1)
            print(f'Knight {self.name} is fighting for {self.days}, enemies left: {self.enemy}')
        print(f'Knight {self.name} conquered all enemies in {self.days} days')


knight1 = Knight('Sir lanselot', 10)
knight2 = Knight('Sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('All battles finished! ')

