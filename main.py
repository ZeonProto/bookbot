def main():
    #   defines book Path
    book_path = "books/frankenstein.txt"
    #   extracts Text from book
    text = get_book_text(book_path)
    #   prints text
    print(text)

def get_book_text(path):
    #   uses the "with" command to open a file in a directory
    with open(path) as f:
        return f.read()


main()