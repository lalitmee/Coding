def balanced(str):
    characters_list = list(set(str))
    frequencies = {}
    for char in range(len(characters_list)):
        count = 0
        for sub_string in range(len(str)):
            if characters_list[char] == str[sub_string]:
                count += 1
                frequencies[characters_list[char]] = count
    unique_frequencies_values = list(set(frequencies.values()))
    if len(unique_frequencies_values) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    str = "x"
    assert balanced("xxxyyyzzz")
    assert balanced("pqq")
    assert balanced("yyyxxx")
    assert balanced("x")
