"""
通用排序：n log n
快速排序，并归排序: 都用到了分类的思维,递归的方法
"""


def merge_sort(data):
    def merge(p, middle, q):
        temp = []
        m = p
        n = middle + 1
        while m <= middle and n <= q:
            if data[m] <= data[n]:
                temp.append(data[m])
                m += 1
            else:
                temp.append(data[n])
                n += 1

        start = m if m <= middle else n
        end = middle if m <= middle else q
        temp.extend(data[start:end + 1])
        data[p:q+1] = temp

    def local_sort(start, end):
        if start == end: return
        middle = (start + end) // 2
        local_sort(start, middle)
        local_sort(middle + 1, end)
        merge(start, middle, end)

    local_sort(0, len(data) - 1)


def quick_sort(data):
    pass


if __name__ == '__main__':
    my_data = [10, 1, 2, -1, 4, 3, 2, 1, 3, 4, 5, 65, 5]
    merge_sort(my_data)
    print(my_data)
