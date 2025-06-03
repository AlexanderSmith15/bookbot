import sys
from stats import word_count, char_count, sorted_count


def get_book_text(file_path):  #opens a text file containing a book and return the book in a string
    book = ""
    with open(file_path) as file:
        book = file.read()
    return book


def main():
    try:
        sys.argv[1] == False
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(sys.argv[1]))} total words\n--------- Character Count -------")
            
    #print(f"{word_count(get_book_text("books/frankenstein.txt"))} words found in the document")
    character_count = char_count(get_book_text(sys.argv[1]))
    #print (character_count)
    sc = sorted_count(character_count)
    for s in sc:
        print(f"{s[0]}: {s[1]}")


main()

