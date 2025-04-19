# Define the mapping
alpha_mapping = {
    'a': '4',
    'b': '6',
    'c': '(',
    'd': 'cl',
    'e': '3',
    'f': 'ph',
    'g': '9',
    'h': '#',
    'i': '!',
    'j': '_|',
    'k': '|(',
    'l': '1',
    'm': 'nn',
    'n': '^',
    'o': '0',
    'p': '|*',
    'q': '<|',
    'r': '2',
    's': '5',
    't': '7',
    'u': 'u',
    'v': 'v',
    'w': 'uu',
    'x': 'x',
    'y': 'j',
    'z': 's'
}

num_mapping = {
    '0': 'O',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g'
}


def print_values(input_str):
    result = ''
    for char in input_str.lower():
        if char.isalpha():
            result += alpha_mapping.get(char, char)
        elif char.isdigit():
            result += num_mapping.get(char, char)
        else:
            result += char
    print(result)


while True:
    input_str = input("Enter a string or 'exit!' to quit): ")
    if input_str.lower() == 'exit!':
        print("Goodbye!")
        break
    print_values(input_str)
