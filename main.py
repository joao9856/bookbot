def main():
    text = text_from_file("books/frankenstein.txt")
    text_len = word_count(text)
    char_count = char_appearence(text)
    conv_dict = conv(char_count)
    conv_dict.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{text_len} words found in the document")
    print()
    
    for char in conv_dict: 
        print(f"The '{char["name"]}' character was found {char["num"]} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def conv(to_conv):
    converted = []
    for char in to_conv:
        if char.isalpha():
            converted.append({"name": char, "num": to_conv[char]})
    return converted


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