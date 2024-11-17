def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        print (len(word_count))

if __name__ == "__main__":
    main()