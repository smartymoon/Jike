"""
通用排序：n log n
快速排序，并归排序: 都用到了分类的思维,递归的方法
"""


def merge_sort(data):
    def local_sort(p, q):
        if q - p == 1:
            if data[q] < data[p]:
                data[q], data[p] = data[p], data[q]
            return
        middle = int((p + q) / 2)
        merge(local_sort(p, middle), local_sort(middle, q))
        while True:
            m, n = p, middle
            if data[m] > data[n]:
                data[m], data[n] = data[n], data[m]
                m += 1



def quick_sort(data):
    pass
