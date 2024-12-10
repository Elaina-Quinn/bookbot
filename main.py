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

# prints results
def results(length, characters):
    print (
        f"--- Begin report of books/frankenstein.txt --- \n {length} words found in the document \n"
    )

    for i in characters:
        print (
            f"The '{i}' character was found {characters[i]} times"
        )



def main():
    file_contents = ""
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()

    results(word_count(file_contents), character_counter(file_contents.lower()))

main()
