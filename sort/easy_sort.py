"""
最简单的排序：n方,适用数据量小
插入排序： 从前向后排,在已排区域找个合适的位置,稳定
选择排序： 从前向后排,在未排区找个合适的元素放在前面,不稳定
冒泡排序： 两两比较，每轮找到一个最大的放在最后,从后向前排,稳定
"""


def bubble_sort(data):
    if len(data) <= 1: return
    for i in range(len(data) - 1):
        has_swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                has_swap = True
        if not has_swap: break


def insertion_sort(data):
    if len(data) <= 1: return
    for i in range(1, len(data)):
        # i循环次数，当前数据索引
        current = data[i]
        j = i - 1
        while current < data[j] and j >= 0:
            # move
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current


def selection_sort(data):
    if len(data) <= 1: return
    for i in range(len(data) - 1):
        # chose small
        most_small_key = i
        most_small_val = data[most_small_key]
        for j in range(i + 1, len(data)):
            if data[j] < most_small_val:
                most_small_key = j
                most_small_val = data[j]
        data[i], data[most_small_key] = most_small_val, data[i]


if __name__ == '__main__':
    my_data = [10, 1, 2, -1, 4, 3, 2, 1, 3, 4, 5, 65, 5]
    selection_sort(my_data)
    print(my_data)
