"""
冒泡排序
"""


def bubble_sort(data):
    for i in range(len(data) - 1):
        has_swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                has_swap = True
        if not has_swap: break


def insert_sort(data):
    pass


if __name__ == '__main__':
    my_data = [10, 1, 2, -1, 4, 3, 2, 1, 3, 4, 5, 65, 5]
    bubble_sort(my_data)
    print(my_data)
