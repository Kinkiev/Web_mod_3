from multiprocessing import Process
import time

def factorize(*numbers):
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
        print (factors)
    return result

if __name__ == '__main__':
    
    numbers = [128, 255, 99999, 10651060]
    processes = []
    start_time = time.time()
    
    for i in numbers:
        pr = Process(target=factorize, args=numbers, )
        pr.start()
        processes.append(pr)
        
    for process in processes:
        process.join()
    
    end_time = time.time()
    
    print (end_time-start_time)  
    print (processes)
    
