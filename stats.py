def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_char_counts(char_count):
    sorted_list = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list