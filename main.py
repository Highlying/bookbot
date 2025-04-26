from stats import get_word_count
from stats import character_dict
# takes a filepath as input and returns the contents of the file as a string.
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(str(get_word_count(text))+" words found in the document."+" \n")
    print("The character count is: " + str(character_dict(text)) + "\n")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()