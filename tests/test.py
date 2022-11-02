import os
import sys
import unittest

sys.path.append(os.getcwd())

from tree import Tree, TestTree, BaseTree
from main import read_files


def ans_class_tree(data, flag: bool):
    ans: list[int] = []
    tec_free: BaseTree
    if flag:
        tec_tree = Tree(data[1])
    else:
        tec_tree = TestTree(data[1])
    for i in range(data[2]):
        tec: list = data[i + 3]
        if tec[0] == 1:
            tec_tree.do_update(tec[1], tec[2], tec[3])
        else:
            ans.append(tec_tree.get_sum(tec[1], tec[2]))
    return ans


class TestSegmentTree(unittest.TestCase):

    def test_correct_ans(self):
        for file in os.listdir('files'):
            data: list = read_files(f'files/{file}')
            ans1: list[int] = ans_class_tree(data, True)
            ans2: list[int] = ans_class_tree(data, False)
            self.assertEqual(len(ans1), len(ans2))
            for i in range(len(ans1)):
                self.assertEqual(ans1[i], ans2[i])


if __name__ == '__main__':
    unittest.main()
