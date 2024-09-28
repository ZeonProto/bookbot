def main():
    #   defines book Path
    book_path = "books/frankenstein.txt"
    #   sends file to "get_book_text" function
    text = get_book_text(book_path)
    #   sends file to "get_word_count" function
    word_count = get_word_count(text)
    #   sends file to "get_character_count" function
    character_count = get_character_count(text)
    #   prints text
    print(character_count)

def get_book_text(path):
    #   uses the "with" command to open a file in a directory
    with open(path) as f:
        #   returns text output to "main" function
        return f.read()

def get_word_count(text):
    #   add the "word_count" tally
    word_count = 0
    #   splits each word individually
    words = text.split()
    #   loop that add 1 to "word_count" for each word
    for i in words:
        word_count += 1
    #   returns the word count to "main" function
    return word_count

def get_character_count(text):
    #   transforms all text to lowercase
    lowered_text = text.lower()
    #   defines the "character_dict" dictionary
    character_dict = {}
    #   separates each letter
    for l in lowered_text:
        #   adds a 1 for each letter that is already present in the dictionary
        if l in character_dict:
            character_dict[l] += 1
        #   creates an entry for that character if it doesn't exist already
        else:
            character_dict[l] = 1
    return character_dict


main()