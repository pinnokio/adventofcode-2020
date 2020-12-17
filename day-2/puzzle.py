#!/usr/bin/env python3

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


def main():
    input = input_read(INPUT_FILE)
    print(validate_passwords(input))


if __name__ == "__main__":
    main()
