from tree import Tree, TestTree


def read_files(file_name: str) -> list:
    with open(file_name) as file:
        array: list = [list(map(int, i.split())) for i in file.readlines()]
        array[0] = int(array[0][0])
        array[2] = int(array[2][0])
        return array


def main():
    file_name = input()
    data: list = read_files(file_name)
    tec_tree: Tree = Tree(data[1])
    for i in range(data[2]):
        tec: list = data[i + 3]
        if tec[0] == 1:
            tec_tree.do_update(tec[1], tec[2], tec[3])
        else:
            print(tec_tree.get_sum(tec[1], tec[2]))


if __name__ == "__main__":
    main()