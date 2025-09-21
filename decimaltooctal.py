def decimal_to_octal(decimal_num):
    if decimal_num == 0:
        return "0"
    octal_num = ""
    while decimal_num > 0:
        octal_num = str(decimal_num % 8) + octal_num
        decimal_num //= 8
    return octal_num

if __name__ == "__main__":
    try:
        decimal_input = int(input("Enter a decimal number: "))
        if decimal_input < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"Octal: {decimal_to_octal(decimal_input)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")