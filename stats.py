def get_book_word_count(text):
    word_count = len(text.split())
    print(f"Found {word_count} total words")

def character_count(text):
    char_count = {}
    character_list = [char for char in text]
    for char in character_list:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return(char_count)

def sort_on(items):
    return items["num"]

def sort_char_count(text):
    list = []
    dictionary = character_count(text)
    for char in dictionary:
        if char.isalpha() == True:
            new_char = {
                "char": char,
                "num": dictionary[char]
            }
            list.append(new_char)
    sorted_list = sorted(list, reverse=True, key=sort_on)
    for char in sorted_list:
        character = char["char"]
        number = char["num"]
        print(f"{character}: {number}")