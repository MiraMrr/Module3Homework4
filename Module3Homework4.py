def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words

result1 = single_root_words('act', 'active', 'artist', 'action', 'agree')
result2 = single_root_words('far', 'firework', 'farewell', 'farther', 'faraway')

print(result1)
print(result2)
