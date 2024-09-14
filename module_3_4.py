def single_root_words(root_words, *other_words):
    same_words = []
    lower_other_words = []
    lower_root_words = root_words.lower()
    for n in range(len(other_words)):
        lowerwords = other_words[n].lower()
        lower_other_words.append(lowerwords)
    for k in range(len(lower_other_words)):
        current_words = lower_other_words[k]
        if len(lower_root_words) < len(current_words):
            if current_words.count(lower_root_words):
                same_words.append(other_words[k])
        if len(lower_root_words) > len(current_words):
            if lower_root_words.count(current_words):
                same_words.append(other_words[k])
    return (same_words)


result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print('result_3: ', result_1)
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print('result_3: ', result_2)
