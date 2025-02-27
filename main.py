from stats import word_count
from stats import char_appearence
from stats import sort_on
from stats import conv
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = text_from_file(sys.argv[1])
    text_len = word_count(text)
    char_count = char_appearence(text)
    conv_dict = conv(char_count)
    conv_dict.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
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