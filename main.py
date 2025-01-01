def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankeinstein.txt")
    print(f"{num_words} words found in the document")
    print()
    char_count = get_char_count(text)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
            
    
main()