from stats import *
import sys

def get_book_text():
    #with open("books/frankenstein.txt") as f:
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

  
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    num_words = get_num_words(get_book_text())
    #print(f"{num_words} words found in the document")
    #print(get_char_count(get_book_text()))
    answer = sort_chars(get_char_count(get_book_text()))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in answer:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["count"]}")
    #char_counts = get_char_count(get_book_text())
    #sorted_chars =sort_chars(char_counts)
    #for char in sorted_chars:
     #   if char.isalpha():
      #      print(char)


main()
