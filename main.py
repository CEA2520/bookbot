def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    report(word_count, char_count)

def get_char_count(text):
    # creates dictionary of alphabet in lowercase
    import string
    char = dict.fromkeys(string.ascii_lowercase, 0)
    # counts instances of each letter
    for i in text:
        if i in string.ascii_lowercase:
            char[i] +=1
    return char

def get_word_count(text):
    # counts the number of words in the document
    words = text.split()
    return len(words)
    

def get_book_text(path):
    # opens the document for program
    with open(path) as f:
        return f.read()

def report(word_count, char_count):
    # Convert dictionary to list of dictionaries
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list by count in descending order
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    # Now loop through our sorted list
    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End Report ---")

main()