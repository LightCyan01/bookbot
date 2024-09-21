with open("./books/frankenstein.txt", "r") as file:
    book = file.read()

def word_count(book):
    words = book.split()
    return len(words)

def character_count(count):
    lower = count.lower()
    char_count = {}
    
    for char in lower:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    char_list = [{"char": key, "count": value} for key, value in char_count.items()]
    return char_list
    
def sort_on(item):
    return item["count"]

def main():
    print("--- Book Statistics ---")
    print(f"{word_count(book)} words found in the document")
    
    count = character_count(book)
    count.sort(reverse=True, key=sort_on)
    
    for item in count:
        print(f"The {item['char']} character was found {item['count']} times")
main()