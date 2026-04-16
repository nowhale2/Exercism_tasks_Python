def generate_seat_letters(number):
    """Generate a series of letters for airline seats.
 
    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.
 
    Seat letters are generated from A to D.
    After D it should start again with A.
 
    Example: A, B, C, D
 
    """
    for i in range(number):
        # Определяем позицию в цикле A‑B‑C‑D (остаток от деления на 4)
        position = i % 4
        # Сопоставляем числовой позиции букву
        if position == 0:
            yield 'A'
        elif position == 1:
            yield 'B'
        elif position == 2:
            yield 'C'
        else:  # position == 3
            yield 'D'

def generate_seats(number):
    """Generate a series of identifiers for airline seats.
 
    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.
 
    A seat number consists of the row number and the seat letter.
 
    There is no row 13.
    Each row has 4 seats.
 
    Seats should be sorted from low to high.
 
    Example: 3C, 3D, 4A, 4B
 
    """
    for i in range(number):
        row = (i // 4) + 1
        if row >= 13:
            row += 1  # учитываем пропуск 13, но это усложняет логику
        letter = 'ABCD'[i % 4]
        yield f"{row}{letter}"


def assign_seats(passengers):
    """Assign seats to passengers.
 
    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.
 
    Example output: {"Adele": "1A", "Björk": "1B"}
 
    """
    seat_generator = generate_seats(len(passengers))
    return dict(zip(passengers, seat_generator))
    
        
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.
 
    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.
 
    """
    for seat_number in seat_numbers:
        code = seat_number + flight_id
        yield f"{code}{'0'*(12 - len(code))}"
