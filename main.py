def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("/Users/marquesb/BootDev/workspace/Bookbot/books/frankenstein.txt")
    numWords = word_count(text)
    print(f"Found {numWords} total words")

main()
