import hashlib
import os
import sys


def check_file(name, alg, h):
    """
    Opens file if it exists and checks if it's hash sum matches the given hash sum.
    """

    try:
        with open(name, 'rb') as file:
            f = file.read()
    except FileNotFoundError:
        print(name + ' NOT FOUND')
        return

    ok = False
    if alg == 'md5':
        ok = (hashlib.md5(f).hexdigest() == h)
    elif alg == 'sha1':
        ok = (hashlib.sha1(f).hexdigest() == h)
    elif alg == 'sha256':
        ok = (hashlib.sha256(f).hexdigest() == h)

    if ok:
        print(name + ' OK')
    else:
        print(name + ' FAIL')


if len(sys.argv) == 3:
    file_path = sys.argv[1]
    dir_path = sys.argv[2]
else:
    print('Usage: python integrity.py <path to the file> <path to the directory>')
    exit()

with open(file_path, 'r') as f:
    lines = f.readlines()

files_list = [line.split(' ') for line in lines]
os.chdir(dir_path)
for file in files_list:
    check_file(file[0], file[1], file[2].rstrip())
