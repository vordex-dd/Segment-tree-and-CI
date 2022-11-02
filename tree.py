class Tree:
    array: list
    peaks: list
    length: int

    def __init__(self, array: list) -> None:
        self.array = array
        self.length = len(self.array)
        self.peaks = [0] * (4 * self.length)
        self.build(1, 0, self.length - 1)

    def build(self, v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.peaks[v] = self.array[tl]
        else:
            tm: int = (tl + tr) // 2
            self.build(2 * v, tl, tm)
            self.build(2 * v + 1, tm + 1, tr)
            self.peaks[v] = self.peaks[2 * v] + self.peaks[2 * v + 1]

    def sum(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.peaks[v]
        tm: int = (tl + tr) // 2
        return self.sum(2 * v, tl, tm, l, min(r, tm)) + self.sum(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)

    def get_sum(self, l: int, r: int) -> int:
        return self.sum(1, 0, self.length - 1, l, r)

    def update(self, v: int, tl: int, tr: int, l: int, r: int, add: int) -> None:
        if l > r:
            return None
        if l == tl and r == tr:
            self.peaks[v] += add * (tr - tl + 1)
        else:
            tm: int = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
            self.peaks[v] = self.peaks[2 * v] + self.peaks[2 * v + 1]

    def do_update(self, l: int, r: int, x) -> None:
        self.update(1, 0, self.length - 1, l, r, x)