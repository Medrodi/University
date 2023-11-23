from get_data import *

if __name__ == '__main__':
    write_to_file(translating(count(morph(get_data("data.txt")))))