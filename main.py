def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    number_of_words = word_count(book_text)
    ch_dictionary = get_characters_dictionary(book_text)
    print_report_by_character(book_path, ch_dictionary, number_of_words)

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        error_message = f"Book not found in {path}"
        print(error_message)
        raise Exception(error_message)

def word_count(text):
    return len(text.split())

def get_characters_dictionary(text):
    character_count = {}

    for ch in text:
        lowered = ch.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1

    return character_count

def print_report_by_character(book_path, ch_dictionary, word_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")

    for ch in ch_dictionary:
        if ch.isalpha():
            print(f"The '{ch}' character was found {ch_dictionary[ch]} times")
    print("--- End report ---")

main()