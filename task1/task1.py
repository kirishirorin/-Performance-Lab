import argparse


def make_path(range_ms):
    path = ''
    for i in range_ms:
        path += str(i[0])
    return path


def circle(n, m):
    circle_arg = list(range(1, n + 1))
    range_ms = []
    while circle_arg:
        range_m = []
        range_m.append(circle_arg[0])
        while len(range_m) < m:
            range_m.append(circle_arg[1])
            circle_arg.append(circle_arg.pop(0))
        if range_m in range_ms:
            break
        else:
            range_ms.append(range_m)
    return make_path(range_ms)


def main():
    parser = argparse.ArgumentParser(description='Круговой массив')
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)
    args = parser.parse_args()
    print(circle(args.n, args.m))


if __name__ == '__main__':
    main()
