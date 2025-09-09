def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as f:
        return f.read()


def get_word_count(book_text):
    return len(book_text.split())


def get_times_character_repeats(book_text):
    character_count = {}

    for char in book_text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count


def get_report(chars_dict):
    sorted_report = dict(
        sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    for report in sorted_report:
        if report.isalpha() and report.isascii():
            print(f"{report}: {sorted_report[report]}")
