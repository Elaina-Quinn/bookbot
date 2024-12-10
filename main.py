# new function to count number of each character in book
# go through each word and add character to running count
    # make a dictionary

# counts words in book
def word_count(book):
    words = book.split()

    return len(words)

# counts how many of each character there is
def character_counter(lowercase_book):
    character_count = {}

    for i in lowercase_book:
        if i in character_count.keys():
            character_count[i] = character_count[i] + 1
        elif i.isalpha():
            character_count[i] = 1

    return character_count


def main():
    file_contents = ""
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()

    print (word_count(file_contents))

    print (character_counter(file_contents.lower()))


main()