import sys
from stats import (
    count_words,
    get_book_text,
    get_char_count,
    char_report,
    print_character_report,
    open_book
    )


def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = open_book(sys.argv[1])#get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    char_count = get_char_count(text)
    #print(f"Found {word_count} total words")
    #print(f"Character list:{char_count}")
    character_report = char_report(char_count)
    print_character_report(word_count,sys.argv[1],character_report)

main()