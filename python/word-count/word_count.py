import re


def word_count(phrase):

    words = re.sub('[^0-9a-zA-Z]+', ' ', phrase).lower().split()
    word_counts = {}
    for word in words:

        if word in word_counts.keys():
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
