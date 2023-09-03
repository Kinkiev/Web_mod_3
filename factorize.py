from multiprocessing import Process, cpu_count
import multiprocessing
import time

cpu = cpu_count()
print (f" your cores number is  - {cpu}")

def factorize(numbers):
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result

# a, b, c, d  = factorize(128, 255, 99999, 10651060)

def time_do():
    numbers = [128, 255, 99990, 10651060]
    start_time = time.time()
    factors_list = factorize(numbers)
    end_time = time.time()
    
    return factors_list, end_time - start_time

if __name__ == '__main__':
    factors_list, execution_time = time_do()

    print(f"Factors: {factors_list}")
    print(f"Execution Time: {execution_time} seconds")

# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]