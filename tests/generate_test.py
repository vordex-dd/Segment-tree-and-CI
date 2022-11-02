from random import randint


def main():
    n, q = map(int, input().split())
    array: list[str] = [str(randint(-100, 10000)) for i in range(n)]
    command: list[str] = []

    for i in range(q):
        status: int = randint(1, 2)
        start: int = randint(0, n - 1)
        finish: int = randint(start, n - 1)
        if status == 1:
            command.append(f'{status} {start} {finish} {randint(-100, 100)}')
        else:
            command.append(f'{status} {start} {finish}')

    string_command: str = '\n'.join(command)
    test_string: str = f'{n}\n{" ".join(array)}\n{q}\n{string_command}'

    with open(f'files/test_{n}_{q}.txt', 'w') as file:
        file.write(test_string)


if __name__ == "__main__":
    main()