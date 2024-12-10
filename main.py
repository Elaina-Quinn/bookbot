def word_count(book):
    words = book.split()

    return len(words)

def main():
    file_contents = ""
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()

    print (word_count(file_contents))


main()