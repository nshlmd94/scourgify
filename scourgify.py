import csv
import string
import sys
import os

def main():
    file_before, file_after = input_validation()
    rearrange(file_before, file_after)
    # this is to avoid the two parameters being considered as a tuple, and therefore, as a single parameter

def input_validation():

    if not len(sys.argv) == 3:
        if len(sys.argv) > 3:
            sys.exit("Too many arguments")
        else:
            sys.exit("Too few arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Wrong filetype")
    
    if not os.access(sys.argv[1], os.R_OK):
        sys.exit("Cannot read file")
    # this is to check if this file can be opened

    file_before = sys.argv[1]
    file_after = sys.argv[2]

    return file_before, file_after

def rearrange(file_before, file_after):

    students = []

    try:
        with open(file_before, "r") as before, open(file_after, "w") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first name", "last name", "house"])
            writer.writeheader()

            for row in reader:
                full_name = row["name"]
                name = full_name.strip().split(",")

                house = row["house"]
                
                writer.writerow({"first name": name[1], "last name": name[0], "house": house})
    
    except FileNotFoundError:
        sys.exit("File not found")

main()