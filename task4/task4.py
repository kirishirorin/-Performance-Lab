import argparse
import math


def nums_into_list(file):
    with open(file, 'r') as file:
        nums_list = list(map(lambda number: int(number[:-1]), file.readlines()))
        return nums_list


def find_min_steps(nums):
    find_avg_num = round(sum(nums) / len(nums))
    count_steps = 0
    for elem in nums:
        count_steps += math.fabs(find_avg_num - elem)
    return int(count_steps)


def main():
    parser = argparse.ArgumentParser(description='Находим минимум ходов')
    parser.add_argument('nums', type=str)
    args = parser.parse_args()
    nums_list = nums_into_list(args.nums)
    print(find_min_steps(nums_list))


if __name__ == '__main__':
    main()
