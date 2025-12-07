def key_func(e):
    return e['count']

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
        if l not in char_dict:
            char_dict[l]=0
        char_dict[l]+=1
    return char_dict

def char_report(char_dict):
    
    dict_list = []
    for i in char_dict.items():
        if str.isalpha(i[0]):
            tmp_dict = {"char":None,"count":None}
            tmp_dict["char"] = i[0]
            tmp_dict["count"]= i[1]
            dict_list.append(tmp_dict)
            
            #dict_list.append(f"{tmp_dict['char']}: {tmp_dict['count']}")
    dict_list.sort(key=key_func,reverse=True)            
    print(dict_list)
    return dict_list

def print_character_report(word_count,path,character_report):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in character_report:
        print(f"{d["char"]}: {d["count"] }")

def open_book(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    pass
    