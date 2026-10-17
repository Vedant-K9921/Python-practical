sentence = input("Enter a sentence: ")

words_list = sentence.split()

if words_list:
    # Find the longest word using max() with key=len
    longest_word = max(words_list, key=len)
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")