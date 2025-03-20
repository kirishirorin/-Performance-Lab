import argparse


def define_point(file1, file2):
    file1 = open(file1, 'r')
    conditions = file1.readlines()
    file1.close()
    x0y0 = conditions[0].split()
    x0 = int(x0y0[0])
    y0 = int(x0y0[1])
    r = int(conditions[1])
    file2 = open(file2, 'r')
    points = file2.readlines()
    file2.close()
    result = ''
    for point in points:
        xy = point.split()
        x = int(xy[0])
        y = int(xy[1])
        if ((x - x0)**2 + (y - y0)**2) ** 0.5 < r:
            result += '1\n'
        elif ((x - x0)**2 + (y - y0)**2) ** 0.5 > r:
            result += '2\n'
        else:
            result += '0\n'
    return result


def main():
    parser = argparse.ArgumentParser(description='Положение точки')
    parser.add_argument('file1', type=str)
    parser.add_argument('file2', type=str)
    args = parser.parse_args()
    print(define_point(args.file1, args.file2))


if __name__ == '__main__':
    main()
