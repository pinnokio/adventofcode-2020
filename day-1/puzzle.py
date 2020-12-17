#!/usr/bin/env python3

import argparse


INPUT_FILE = "input.txt"


def input_read(input_file):
    with open(input_file, 'r') as input_file:
        input = [int(row) for row in input_file]
    # input_file.close()
    return input


def part_one(input_file):
    input = input_read(input_file)
    for i in range(len(input)) :
        for j in range(i + 1, len(input)):
            if (input[i] + input[j]) == 2020:
                return input[i] * input[j]


def part_two(input_file):
    input = input_read(input_file)
    for i in range(len(input)) :
        for j in range(i + 1, len(input)):
            if (input[i] + input[j]) == 2020:
                return input[i] * input[j]


def main():
    parser = argparse.ArgumentParser(description="Enter day number")
    parser.add_argument(
            "number",
            type=int,
            help="index number of a day's puzzle",
            choices=[1, 2],
            )
    args = parser.parse_args()
    if args.number == 1:
        print("Answer: {}".format(part_one(INPUT_FILE)))

if __name__=="__main__":
    main()

