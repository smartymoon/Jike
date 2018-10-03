import time
if __name__ == '__main__':

    # list
    list = [i for i in range(1000000)]

    start = time.process_time()
    for index in range(1000000):
        list[index] += 1

    # array

    '''
    ar = array.array('L', [i for i in range(1000000)])
    start = time.process_time()
    for index in range(1000000):
        ar[index] += 1
    '''

    end = time.process_time()
    print(end - start)
