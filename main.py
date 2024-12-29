def main():
    text = text_from_file("books/frankenstein.txt")
    text_len = word_count(text)
    char_count = char_appearence(text)
    print(char_count)


def text_from_file(path):
    with open(path) as f:
        return f.read()

def word_count(to_count):
    return len(to_count.split())

def char_appearence(to_count_char):
    char_count = {}
    lower_case_text = to_count_char.lower()
    for char in lower_case_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
main()