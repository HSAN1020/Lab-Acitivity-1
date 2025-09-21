def main():
    filename = input("Enter the filename: ")
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except:
        print("Error: File could not be read")
        return

    num_lines = len(lines)

    if num_lines == 0:
        print("The file is empty.")
        return

    while True:
        print("\nThe file has", num_lines, "lines. ")
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Not a valid number.")
            continue

        if line_number == 0:
            print("Goodbye")
            break

        if line_number < 1 or line_number > num_lines:
            print("Invalid line number. Please enter a number between 1 and", num_lines)
        else:
            print("Line", line_number, ":", lines[line_number - 1], end='')

main()