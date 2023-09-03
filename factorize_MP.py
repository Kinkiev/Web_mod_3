import multiprocessing
import time

def factorize_worker(num, result_dict):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    result_dict[num] = factors if factors else [num]

def factorize_parallel(numbers):
    manager = multiprocessing.Manager()
    result_dict = manager.dict()
    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=factorize_worker, args=(num, result_dict))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return [result_dict[num] for num in numbers]

def time_do():
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()
    factors_list = factorize_parallel(numbers)
    end_time = time.time()
    
    return factors_list, end_time - start_time

if __name__ == '__main__':
    factors_list, execution_time = time_do()

    print(f"Factors for 128: {factors_list[0]} \n")
    print(f"Factors for 256: {factors_list[1]} \n")
    print(f"Factors for 99999: {factors_list[2]} \n")
    print(f"Factors for 10651060: {factors_list[3]} \n")
    print(f"Execution Time: {execution_time} seconds \n")
    
    a = [1, 2, 4, 8, 16, 32, 64, 128]
    b = [1, 3, 5, 15, 17, 51, 85, 255]
    c = [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    d = [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    assert a == factors_list[0]
    assert b == factors_list[1]
    assert c == factors_list[2]
    assert d == factors_list[3]