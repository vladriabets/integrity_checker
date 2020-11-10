import hashlib
import os
import sys


def read_file(path_to_file, mode="rb", by_lines=False):

    """ Read file if it exists. """

    try:
        if by_lines:
            with open(path_to_file, mode, 1) as file:
                f = file.readlines()
        else:
            with open(path_to_file, mode, 1) as file:
                f = file.read()
        return f
    except FileNotFoundError:
        print(path_to_file + " NOT FOUND")


def check_file_hash(path_to_file, alg, h):

    """ Compare file's hash sum with the given argument. """

    ok = False
    file = read_file(path_to_file, "rb")
    if file:
        if alg == "md5":
            ok = (hashlib.md5(file).hexdigest() == h)
        elif alg == "sha1":
            ok = (hashlib.sha1(file).hexdigest() == h)
        elif alg == "sha256":
            ok = (hashlib.sha256(file).hexdigest() == h)

        if ok:
            print(path_to_file + " OK")
        else:
            print(path_to_file + " FAIL")


def main():

    """
    You give 2 arguments:
        1. Path to the file with the list of files, algorithms and hash sums.
        2. Path to the directiry with files you want to check.
    Each line in the file with the list should be formatted like this:
        file_name algorithm hash_sum

    The script checks file's hash for each one in the file's list.
    """

    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        dir_path = sys.argv[2]
    else:
        print("Usage: python integrity.py <path to the file> <path to the directory>")
        exit(1)

    lines = read_file(file_path, "r", by_lines=True)
    files_list = [line.split(" ") for line in lines]

    os.chdir(dir_path)

    for file in files_list:
        try:
            check_file_hash(file[0], file[1], file[2].rstrip())
        except IndexError:
            print("Wrong file's list format.")

if __name__ == "__main__":
    main()
