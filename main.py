from stats import count_text, count_character, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

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
print(f"Analyzing book found at {filepath}")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char in result:
    if not char["char"].isalpha():
        continue
    else:
        print(f"{char["char"]}: {char["num"]}")
print("============= END ===============")
