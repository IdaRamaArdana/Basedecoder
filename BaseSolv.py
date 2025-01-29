def convert_base(input_value, input_base, output_base):
    """
    Converts a number from one base to another.
    Supports binary (base 2), decimal (base 10), and hexadecimal (base 16).

    :param input_value: The input value as a string (e.g., "1010", "1A", "26").
    :param input_base: The base of the input value (2, 10, or 16).
    :param output_base: The base to convert to (2, 10, or 16).
    :return: The converted value as a string.
    """
    try:
        # Validate input and output bases
        if input_base not in [2, 10, 16] or output_base not in [2, 10, 16]:
            raise ValueError("Unsupported base. Use 2 (binary), 10 (decimal), or 16 (hexadecimal).")

        # Convert input value to decimal (base 10)
        if input_base == 2:
            decimal_value = int(input_value, 2)  # Binary to decimal
        elif input_base == 10:
            decimal_value = int(input_value)  # Decimal to decimal
        elif input_base == 16:
            decimal_value = int(input_value, 16)  # Hexadecimal to decimal

        # Convert decimal value to the desired output base
        if output_base == 2:
            return bin(decimal_value)[2:]  # Decimal to binary
        elif output_base == 10:
            return str(decimal_value)  # Decimal to decimal
        elif output_base == 16:
            return hex(decimal_value)[2:].upper()  # Decimal to hexadecimal

    except ValueError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    input_value = input("Enter the value to convert: ")
    input_base = int(input("Enter the base of the input value (2 for binary, 10 for decimal, 16 for hexadecimal): "))
    output_base = int(input("Enter the base to convert to (2 for binary, 10 for decimal, 16 for hexadecimal): "))

    result = convert_base(input_value, input_base, output_base)
    print(f"Converted value: {result}")
