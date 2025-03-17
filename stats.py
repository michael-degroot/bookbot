import string

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_char_count(text):
    low_text = text.lower()
    char_counts = {}
    for i in string.printable:
        char_count = low_text.count(i)
        char_counts[i] = char_count
    return char_counts

def sort_chars(chars):
    chars_list = []
    for key, value in chars.items():
        chars_list.append({"char" : key, "count" : value})
    chars_list.sort(key = lambda x: x["count"], reverse=True)
    return chars_list
    #Sort dictionary items by value in descending order
    #sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    #return sorted_chars

