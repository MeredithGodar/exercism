from itertools import groupby
import re


def encode(string_to_encode):
    output = ''

    for total, character in [(len(list(g)), k) for k, g in groupby(string_to_encode)]:
        if total == 1:
            output += character
        else:
            output += str(total) + character

    return output


def decode(string_to_decode):
    output = ''

    for count, char in decode_helper(string_to_decode):
        if count.isdigit():
            output += int(count) * char
        else:
            output += char

    return output


def decode_helper(string_to_decode):
    return map(lambda x: [re.match('\d*', x).group(), x[-1]], re.findall('(\d*\D)', string_to_decode))
