def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    #print(book_text)
    print("--- Begin report of books/frankenstein.txt ---")
    get_book_characters(book_path)
    get_book_count_characters(book_path)
    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_book_characters(book_path):
    with open(book_path) as f:
        words = f.read().split()
        print(f"{len(words)} words found in the document")
        print()

def get_book_count_characters(book_path):
    x = 0
    with open(book_path) as f:
        file_contents = f.read().lower()
        book_count_characters_dict = {}
        for c in file_contents:
            if c in book_count_characters_dict and c.isalpha() == True:
                book_count_characters_dict[c] += 1
            else:
                if c.isalpha() == True:
                    book_count_characters_dict[c] = 1
        book_count_characters_dict = dict(sorted(book_count_characters_dict.items(), key=lambda item: item[1],reverse=True))
        for i in book_count_characters_dict:
            print(f"The '{i}' character was found {book_count_characters_dict[i]} times")
            x +=1
        #print(book_count_characters_dict)
        #return book_count_characters_dict

main()