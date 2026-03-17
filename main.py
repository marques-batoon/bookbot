from stats import word_count, char_count, sort_on

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
    char_list = char_count(text)
    char_list_sorted = dict(sorted(char_list.items()))
    for key, value in char_list_sorted.items():
        print(f"{key}: {value}")
    print("============= END ===============")


main()
