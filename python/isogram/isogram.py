def is_isogram(phrase):
    found_letters = []

    if phrase.strip() == "":
        return True
    else:
        for character in phrase.strip().lower():
            if character.isalpha():
                if character in found_letters:
                    return False
                else:
                    found_letters.append(character)

    return True
