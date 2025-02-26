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


def sort_on(dict):
    return dict["num"]


def conv(to_conv):
    converted = []
    for char in to_conv:
        if char.isalpha():
            converted.append({"name": char, "num": to_conv[char]})
    return converted