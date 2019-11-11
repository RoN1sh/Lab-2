alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїклмнопрстухфцчшщьюя"
text = input("Enter your text: ")
for char in alphabet:
    count = text.count(char)
    if count > 0:
        print(char, count)