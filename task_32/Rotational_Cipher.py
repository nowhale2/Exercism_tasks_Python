def rotate(text, key):
    plain_lower = "abcdefghijklmnopqrstuvwxyz"
    plain_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = {}
    text_new = ""
    for i, char in enumerate(plain_lower):
        shifted_index = (i + key) % len(plain_lower)
        cipher[char] = plain_lower[shifted_index]
    for i, char in enumerate(plain_upper):
        shifted_index = (i + key) % len(plain_upper)
        cipher[char] = plain_upper[shifted_index]
    for char in text:
        if char.isalpha():
            text_new += cipher[char]
        else:
            text_new += char
    return text_new
