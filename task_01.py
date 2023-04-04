def has_rhythm(text, return_counts=False):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    counts = [{letter: word.count(letter) for letter in word if letter in vowels} for word in text.split()]

    l = [sum(s.values()) for s in counts]
    rhythm = all(l[i] == l[i + 1] for i in range(len(l) - 1))

    return (rhythm, counts) if return_counts else rhythm

words = "пара-ра-рам рам-пуум-пупам па-ре-по-дам"
print(has_rhythm(words, True))
