from stats import word_count
from stats import char_appearence
from stats import sort_on
from stats import conv


def main():
    text = text_from_file("books/frankenstein.txt")
    text_len = word_count(text)
    char_count = char_appearence(text)
    conv_dict = conv(char_count)
    conv_dict.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("--- Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {text_len} total words")
    print("--------- Character Count -------")
    
    for char in conv_dict: 
        print(f"{char["name"]}: {char["num"]}")

    print("============= END ===============")


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


main()