
import sys
from stats import count_words, count_characters, get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File {book_path} not found")
        sys.exit(1)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = get_sorted_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()