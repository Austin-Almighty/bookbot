from stats import count_text, count_character, sort_dict

filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print(get_book_text(filepath))


word_count = count_text(get_book_text(filepath))

tally = count_character(get_book_text(filepath))

# print(word_count)
# print(tally)


result = sort_dict(tally)

print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char in result:
    if not char["char"].isalpha():
        continue
    else:
        print(f"{char["char"]}: {char["num"]}")
print("============= END ===============")
