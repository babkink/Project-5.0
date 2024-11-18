import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for lines in file:
            if file.readline() != '':
                all_data.append(file.readline()+'\n')


files_ = [f'file {number}.txt' for number in range(1, 5)]

# start_ = time.time()
# for file in files_:
#     read_info(file)
# end_ = time.time()
# print(f'time for linear approach = {(end_ - start_):.2f}')

if __name__ == '__main__':
    start_ = time.time()
    with Pool() as pool:
        res = pool.map(read_info, files_)
    end_ = time.time()
    print(f'time for concurrent approach = {(end_ - start_):.2f}')