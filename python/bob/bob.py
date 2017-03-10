# -*- coding: utf-8 -*-

import re
import unicodedata


def hey(what):

    if what.strip() == '':
        return 'Fine. Be that way!'
    elif what.strip().endswith('?') and not is_shouting(what):
        return 'Sure.'
    elif is_shouting(what):
        response = 'Whoa, chill out!'

        for c in what:
            if unicodedata.category(c) == 'Ll':
                response = 'Whatever.'

        return response
    else:
        return 'Whatever.'


def is_shouting(what):
    alpha_character_substring = re.sub(r'[^a-zA-Z]', '', what)
    uppercase_substring = [l for l in alpha_character_substring if l.isupper()]

    return len(uppercase_substring) == len(alpha_character_substring) and len(uppercase_substring) != 0
