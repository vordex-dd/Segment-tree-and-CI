import abc


class BaseTree(abc.ABC):
    array: list
    length: int

    def __init__(self, array: list) -> None:
        self.array = array.copy()
        self.length = len(self.array)

    @abc.abstractmethod
    def get_sum(self, l: int, r: int) -> int:
        raise NotImplemented

    @abc.abstractmethod
    def do_update(self, l: int, r: int, add: int) -> None:
        raise NotImplemented


class Tree(BaseTree):
    peaks: list
    add_peaks: list

    def __init__(self, array: list) -> None:
        super().__init__(array)
        self.peaks = [0] * (4 * self.length)
        self.add_peaks = [0] * (4 * self.length)
        self.build(1, 0, self.length - 1)

    def build(self, v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.peaks[v] = self.array[tl]
        else:
            tm: int = (tl + tr) // 2
            self.build(2 * v, tl, tm)
            self.build(2 * v + 1, tm + 1, tr)
            self.peaks[v] = self.peaks[2 * v] + self.peaks[2 * v + 1]

    def sum(self, v: int, tl: int, tr: int, l: int, r: int) -> (int, int):
        if l > r:
            return 0, 0
        if l == tl and r == tr:
            return self.peaks[v], tr - tl + 1
        tm: int = (tl + tr) // 2
        val1: (int, int) = self.sum(2 * v, tl, tm, l, min(r, tm))
        val2: (int, int) = self.sum(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        return val1[0] + val2[0] + self.add_peaks[v] * (val1[1] + val2[1]), val1[1] + val2[1]

    def get_sum(self, l: int, r: int) -> int:
        return self.sum(1, 0, self.length - 1, l, r)[0]

    def update(self, v: int, tl: int, tr: int, l: int, r: int, add: int) -> None:
        if l > r:
            return None
        if l == tl and r == tr:
            self.add_peaks[v] += add
            self.peaks[v] += add * (tr - tl + 1)
            return None
        tm: int = (tl + tr) // 2
        self.update(2 * v, tl, tm, l, min(r, tm), add)
        self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
        self.peaks[v] = self.peaks[2 * v] + self.peaks[2 * v + 1] + self.add_peaks[v] * (tr - tl + 1)

    def do_update(self, l: int, r: int, x) -> None:
        self.update(1, 0, self.length - 1, l, r, x)


class TestTree(BaseTree):

    def get_sum(self, l: int, r: int) -> int:
        return sum(self.array[l:r + 1])

    def do_update(self, l: int, r: int, add: int) -> None:
        for i in range(l, r + 1):
            self.array[i] += add
