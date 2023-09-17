def count_letters(word):
    count = {}
    for letter in word:
        count[letter.lower()] = count.get(letter.lower(), 0) + 1
    for key, value in count.items():
        print(key, value)
word = 'Абу'
count_letters(word)