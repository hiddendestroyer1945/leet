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

# Create reverse mappings
reverse_alpha_mapping = {}
for key, value in alpha_mapping.items():
    reverse_alpha_mapping[value.lower()] = key

reverse_num_mapping = {}
for key, value in num_mapping.items():
    reverse_num_mapping[value.lower()] = key


def leet_to_text(leet_text):
    text = ''
    i = 0
    while i < len(leet_text):
        found = False
        for key in sorted(reverse_alpha_mapping.keys(), key=len, reverse=True):
            if leet_text[i:].lower().startswith(key):
                text += reverse_alpha_mapping[key]
                i += len(key)
                found = True
                break
        if not found:
            if leet_text[i].lower() in reverse_num_mapping:
                text += reverse_num_mapping[leet_text[i].lower()]
            else:
                text += leet_text[i]
            i += 1
    return text


while True:
    leet_text = input("Enter leetspeak text or 'exit!' to quit): ")
    if leet_text.lower() == 'exit!':
        print("Goodbye!")
        break
    print(leet_to_text(leet_text))
