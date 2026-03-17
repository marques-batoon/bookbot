from stats import word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("/Users/marquesb/BootDev/workspace/Bookbot/books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    numWords = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    print(char_count(text))

main()
