from stats import get_word_count
from stats import get_times_character_repeats
from stats import get_book_text
from stats import get_report

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    chars_dict = get_times_character_repeats(book_text)

    # num_words = get_word_count(book_text)
    # print(f"{num_words} words found in the document")
    
    # character_count = get_times_character_repeats(book_text)
    # print(character_count)
    print("===== BOOK BOT =====")
    print(f"Analyzing book found at {book_path}")
    print("----- Word Count -----")
    
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")
    

    print("----- Character Count -----")
    get_report(chars_dict)
    print("===== END =====")


main()

