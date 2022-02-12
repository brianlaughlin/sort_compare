'''
Python sort comparison
'''

import random
import time

# create a list of random numbers between 1 and 1000 with a len of 20000
random_list = [random.randint(1, 1000) for i in range(20000)]

# Bubble Sort
def bubble_sort(random_list):
    for _ in range(len(random_list)):
        for j in range(len(random_list) - 1):
            if random_list[j] > random_list[j + 1]:
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
    return random_list

# Selection Sort
def selection_sort(random_list):
    for i in range(len(random_list)):
        min_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[min_index] > random_list[j]:
                min_index = j
        random_list[i], random_list[min_index] = random_list[min_index], random_list[i]
    return random_list

# Counting Sort
def counting_sort(random_list):
    # create a list of 0's with a len of the max value in the list
    count_list = [0] * (max(random_list) + 1)
    for i in range(len(random_list)):
        count_list[random_list[i]] += 1
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]
    sorted_list = [0] * len(random_list)
    for i in range(len(random_list) - 1, -1, -1):
        sorted_list[count_list[random_list[i]] - 1] = random_list[i]
        count_list[random_list[i]] -= 1
    return sorted_list

def python_sort(random_list):
    return sorted(random_list)


def __main__():
    start_time = time.time()
    bubble_sort(random_list)
    end_time = time.time()
    print(f'Bubble Sort took {end_time - start_time} seconds to sort')

    start_time = time.time()
    selection_sort(random_list)
    end_time = time.time()
    print(f'Selection Sort took {end_time - start_time} seconds to sort')

    start_time = time.time()
    python_sort(random_list)
    end_time = time.time()
    print(f'Python Sort took {end_time - start_time} seconds to sort')

    start_time = time.time()
    counting_sort(random_list)
    end_time = time.time()
    print(f'Counting Sort took {end_time - start_time} seconds to sort')


if __name__ == '__main__':
    __main__()





