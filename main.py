def main():
    #   defines book Path
    book_path = "books/frankenstein.txt"
    #   sends file to "get_book_text" function
    text = get_book_text(book_path)
    #   sends file to "get_word_count" function
    word_count = get_word_count(text)
    #   prints text
    print(text, word_count)

def get_book_text(path):
    #   uses the "with" command to open a file in a directory
    with open(path) as f:
        #   returns text output to "main" function
        return f.read()

def get_word_count(path):
    #   add the 'word_count' tally
    word_count = 0
    #   splits each word individually
    words = path.split()
    #   loop that add 1 to 'word_count' for each word
    for i in words:
        word_count += 1
    return word_count

main()