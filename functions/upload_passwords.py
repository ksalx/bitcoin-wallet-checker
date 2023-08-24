from itertools import islice


def get_passwords(filename: str, count_passwords: int):
    try:
        with open(filename, 'r') as file:
            while next_count_passwords := list(islice(file, count_passwords)):
                yield [x.rstrip() for x in next_count_passwords]
    except FileNotFoundError:
        print('File "passwords.txt" with passwords not found')
