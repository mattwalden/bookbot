def count_words(book_text):
    split_text = book_text.split()
    return len(split_text)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_char_count(book_text):
    char_dict = dict()
    text=book_text.lower()
    for l in text:
        k=char_dict.keys()
        if l not in k:
            char_dict.l = 1
        else:
            x =char_dict.values()
            current = char_dict[l]
            char_dict[l]= current + 1

    return char_dict
# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change
    pass
    