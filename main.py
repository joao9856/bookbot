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
    split_text = lower_case_text.split()
    for i in range(len(split_text)):
        if len(split_text[i]) > 1:
            tmp_split = split_text[i]
            for o in range(len(split_text[i])):
                if tmp_split[o] in char_count:
                    char_count[tmp_split[o]] += 1
                else:
                    char_count[tmp_split[o]] = 1
        else:
            if split_text[i] in char_count:
                char_count[split_text[i]] += 1
            else:
                char_count[split_text[i]] = 1
    return char_count
main()