def is_armstrong_number(number):
    str_num = str(number)
    num_digits = len(str_num)  # количество цифр
    
    # Суммируем каждую цифру, возведённую в степень num_digits
    total = sum(int(digit) ** num_digits for digit in str_num)
    
    # Сравниваем сумму с исходным числом
    return total == number
