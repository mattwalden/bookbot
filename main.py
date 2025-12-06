from stats import count_words,get_book_text,get_char_count



def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    get_char_count(text)
    print(f"Found {word_count} total words")

main()
