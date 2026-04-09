import re
def response(hey_bob):
    pattern = r"\?\s*$"
    
    if not hey_bob or hey_bob.isspace():
        return "Fine. Be that way!"
    # We check whether the message ends with a question mark
    end_str = bool(re.search(pattern, hey_bob))
    is_question = end_str
    # We check whether the message is written entirely in capital letters (for alphabetic characters only)
    has_letters = any(letter.isalpha() for letter in hey_bob)
    is_shouting = has_letters and hey_bob.isupper()
    # The logic of decision making
    if is_question and is_shouting:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_shouting:
        return "Whoa, chill out!"
    return "Whatever."
