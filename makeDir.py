import os
import sys

def make_at(path,dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    finally:
        os.chdir(original_path)

if __name__ == "__main__":
    make_at(sys.argv[1],sys.argv[2])