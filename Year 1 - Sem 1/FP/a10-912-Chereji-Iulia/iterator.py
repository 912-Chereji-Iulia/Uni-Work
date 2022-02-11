
class IterableObject:
    class Iterator:
        def __init__(self, col):
            self._collection = col
            self._poz = 0

        def __next__(self):
            if self._poz == len(self._collection.data):
                raise StopIteration()
            self._poz += 1
            return self._collection.data[self._poz - 1]

    def __init__(self):
        self.data = []

    def __iter__(self):
        return self.Iterator(self)

    def add(self, elem):
        self.data.append(elem)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)


def shell_sort(array, sort_key):
    n = len(array)
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
            aux = array[i]

            j = i
            while j >= gap and sort_key(aux, array[j - gap]):
                array[j] = array[j-gap]
                j -= gap

            array[j] = aux

        gap //= 2


def _filter(array, condition):
    res_array = [v for v in array if condition(v)]
    return res_array
