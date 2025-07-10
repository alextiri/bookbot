from stats import get_book_word_count, character_count, sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    get_book_word_count(book_text)
    # print(character_count(book_text))
    sort_char_count(book_text)
main()
