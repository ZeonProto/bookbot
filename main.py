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
    sorted_char_dict = sort_char_dict(character_count)
    print(f"{word_count} words found in the document")

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
    #   defines the "character_dict" dictionary
    character_dict = {}
    #   separates each character
    for char in text:
        #   sets all characters to lower case
        lowered = char.lower()
        #   adds a 1 for each letter that is already present in the dictionary
        if lowered in character_dict:
            character_dict[lowered] += 1
        #   creates an entry for that character if it doesn't exist already
        else:
            character_dict[lowered] = 1
    #   returns the character count to "main" function
    return character_dict

def sort_char_dict(list):
    sorted_character_dict = []
    for char in list:
        if char.isalpha() == True:
            sorted_character_dict.append(char)
    print(sorted_character_dict)


main()