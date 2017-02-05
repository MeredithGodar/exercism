def distance(this, that):

    if len(this) is not len(that):
        raise ValueError

    hamming_dist = 0
    for i in range(0, len(this), 1):
        if this[i] is not that[i]:
            hamming_dist += 1

    return hamming_dist
