with open("sample.txt", "r") as file:
    content = file.read()
    words_list = content.split()

print(f"i. Total number of words: {len(words_list)}")

unique_words = list(set(words_list))
print(f"ii. Unique words: {unique_words}")