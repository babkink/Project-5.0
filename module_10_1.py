import time
from time import sleep
import threading

def write_words(word_count, file_name):
    f = open(file_name, 'w')
    for i in range(word_count):
        f.writelines(f'Some word #{i}\n')
        sleep(0.1)
    print(f'Record to the file "{file_name}" finished')
    f.close()

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f'Writing time to the files: {(end_time - start_time):.2f}')

start_time = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time = time.time()
print(f'Writing time to the files: {(end_time - start_time):.2f}')