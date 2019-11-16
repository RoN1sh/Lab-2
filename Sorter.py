input_list = input("Enter some words: ")
words = input_list.split()
words.sort()
print("Yours sorted words: ")
for word in words:
    print(word)
