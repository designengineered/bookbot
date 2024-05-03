def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_freq = get_chars_dict(text)
    sorted_chars = chars_dict_to_sort_list(char_freq)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_chars(d):
    return d["num"]


def chars_dict_to_sort_list(char_freq):
    sorted_list = []
    for ch in char_freq:
        sorted_list.append({"char": ch, "num": char_freq[ch]})
    sorted_list.sort(reverse=True, key=sort_chars)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars


def get_word_count(text):
    words = text.split()
    w_count = len(words)
    return w_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
