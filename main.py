#   function to print the information to the terminal using all the availible information
def main():
    #   defines book Path
    book_path = "books/frankenstein.txt"
    #   sends file to "get_book_text" function
    text = get_book_text(book_path)
    #   sends file to "get_word_count" function
    word_count = get_word_count(text)
    #   sends file to "get_character_count" function
    character_count = get_character_count(text)
    #   sends the character count dictionary to "sort_char_list" function
    sorted_character_list = sort_char_list(character_count)

    #   prints report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in sorted_character_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End Report ---")

#   function to extract the text from the .txt file
def get_book_text(path):
    #   uses the "with" command to open a file in a directory
    with open(path) as f:
        #   returns text output to "main" function
        return f.read()
    
#   function to get the word count for the text
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

#   function to get the individual character count from the text
def get_character_count(text):
    #   defines the "character_dict" dictionary
    character_dict = {}
    #   separates each character
    for char in text:
        #   sets all characters to lower case
        lowered = char.lower()
        #   checks if the character is a letter and eliminates number or dots
        if char.isalpha() == True:
            #   adds a 1 for each letter that is already present in the dictionary
            if lowered in character_dict:
                character_dict[lowered] += 1
            #   creates an entry for that letter if it doesn't exist already
            else:
                character_dict[lowered] = 1
    #   returns the character count to "main" function
    return character_dict

#   function to sort the "sorted_list" list from most to least used character
def sort_on(d):
    return d["num"]

#   function to use the dictionary "character_dict" to create a list and separate the entries in text e amount
def sort_char_list(dict):
    #   defines the "sorted_list" list
    sorted_list = []
    #   for each entry in the "dict" dictionary creates an entry in the "sorted_list" list with a "char" and "num" denominator
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    #   uses the "sort_on" function to sort the list from most to least used character
    sorted_list.sort(reverse=True, key=sort_on)
    #   returns the list to the "main" function
    return sorted_list

main()