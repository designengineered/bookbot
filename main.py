def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"There are {word_count} words in this document.")


def get_word_count(text):
    words = text.split()
    w_count = len(words)
    return w_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
