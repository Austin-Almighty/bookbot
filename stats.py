def count_text(text):
    count = len(text.split())
    # print(f"{count} words found in the document")
    return count

def count_character(text):
    count_dict = {}
    for char in text:
        if char.lower() in count_dict:
            count_dict[char.lower()] += 1
        else:
            count_dict[char.lower()] = 1
    return count_dict

def sort_dict(char_dic):
    char_list = []

    for keys, values in char_dic.items():
        character = {"char":keys, "num":values}
        char_list.append(character)

    def sort_on(characters):
        return characters["num"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
    
    
