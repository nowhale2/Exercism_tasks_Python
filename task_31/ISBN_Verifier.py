def is_valid(isbn):
    cleaned = isbn.replace('-', '').replace(' ', '').upper()
    if len(cleaned) != 10:
        return False
    total = 0
    for i, char in enumerate(cleaned):
        position = 10 - i  # вес: 10, 9, ..., 1
        if i == 9 and char == 'X':
            total += 10 * position
        elif char.isdigit():
            total += int(char) * position
        else:
            return False
    return total % 11 == 0
