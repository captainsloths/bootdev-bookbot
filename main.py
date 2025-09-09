from stats import get_word_count
from stats import get_times_character_repeats
from stats import get_book_text
from stats import get_report
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Use the second argument in sys.argv as the path to the book file
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    chars_dict = get_times_character_repeats(book_text)

    print("===== BOOK BOT =====")
    print(f"Analyzing book found at {book_path}")
    print("----- Word Count -----")
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")
    print("----- Character Count -----")
    get_report(chars_dict)
    print("===== END =====")


main()
