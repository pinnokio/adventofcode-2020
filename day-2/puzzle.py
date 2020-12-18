#!/usr/bin/env python3

import argparse


INPUT_FILE = "input"


def parse_input(line):
    pw_row = {}
    raw = line.split(" ")
    pw_row["min"], pw_row["max"] = raw[0].split("-")
    pw_row["char"] = raw[1].strip(":")
    pw_row["pw"] = raw[2].strip("\n")
    return pw_row


def input_read(input_file):
    input = []
    with open(input_file, "r") as input_file:
        input = [parse_input(line) for line in input_file]
    return input


def validate_passwords(passwords):
    valid_passwords_count = 0
    for item in passwords:
        if item["char"] in item["pw"]:
            count = 0
            pos = item["pw"].find(item["char"])
            while pos != -1:
                count += 1
                pos = item["pw"].find(item["char"], pos+1)
            if int(item["min"]) <= count <= int(item["max"]):
                valid_passwords_count += 1
    return valid_passwords_count


def validate_passwords_2(passwords):
    valid_passwords_count = 0
    for item in passwords:
        if item["char"] in item["pw"]:
            count = 0
            pos = item["pw"].find(item["char"])
            fchar = int(item["min"]) - 1
            schar = int(item["max"]) - 1
            while pos != -1:
                if pos in [fchar, schar]:
                    count += 1
                pos = item["pw"].find(item["char"], pos+1)
        if count == 1:
            valid_passwords_count += 1
    return valid_passwords_count


# def validate_passwords_2(passwords):
#     valid_passwords_count = 0
#     for item in passwords:
#         if item["char"] in item["pw"]:
#             fchar = int(item["min"]) - 1
#             schar = int(item["max"]) - 1
#             if (item["pw"].find(item["char"], fchar, fchar) == -1 or
#                     item["pw"].find(item["char"], schar, schar) == -1):
#                 valid_passwords_count += 1
#                 print("Char: {} in {} pos_min: {} pos_max {}".format(item["pw"], item["char"], item["min"], item["max"]))
#     return valid_passwords_count


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
        print(validate_passwords(input_read(INPUT_FILE)))
    if args.number == 2:
        print(validate_passwords_2(input_read(INPUT_FILE)))


if __name__ == "__main__":
    main()

