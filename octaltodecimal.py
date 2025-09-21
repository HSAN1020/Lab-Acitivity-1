def octal_to_decimal(octal_str):
    try:
        # Validate octal input
        if not all(char in "01234567" for char in octal_str):
            return "Invalid octal number."
        decimal_num = 0
        for digit in octal_str:
            decimal_num = decimal_num * 8 + int(digit)
        return decimal_num
    except ValueError:
        return "Invalid input."

if __name__ == "__main__":
    octal_input = input("Enter an octal number: ")
    result = octal_to_decimal(octal_input)
    print(f"Decimal: {result}")