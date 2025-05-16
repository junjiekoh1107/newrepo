def largest_series_product(digits: str, length: int) -> int:
    """
    Calculates the largest product from all contiguous series of a specified length in a digit string.

    Parameters:
        digits (str): A string of digits only.
        length (int): Length of the series.

    Returns:
        int: The largest product found among all possible series.

    Raises:
        ValueError: For invalid input conditions.
    """
    if not digits:
        raise ValueError("sequence input must not be empty")

    if not digits.isdigit():
        raise ValueError("sequence input must only contain digits")

    if len(digits) == 0:
        raise ValueError("sequence input must be greater than 0")

    if length < 0:
        raise ValueError("length must not be negative")

    if length == 0:
        raise ValueError("length must be greater than 0")

    if length > len(digits):
        raise ValueError("length must be smaller than string length")

    max_product = 0

    for i in range(len(digits) - length + 1):
        series = digits[i:i + length]
        product = 1
        for char in series:
            product *= int(char)
        max_product = max(max_product, product)

    return max_product


def prompt_for_digits() -> str:
    while True:
        digits = input("Enter any digit sequence: ").strip()
        if not digits:
            print("🚫 Error: Input cannot be empty.")
        elif not digits.isdigit():
            print("🚫 Error: Input must only contain digits (0–9).")
        elif int(digits) == 0:
            print("🚫 Error: Input value must be greater than 0 (not just zeros).")
        else:
            return digits


def prompt_for_length(digits: str) -> int:
    while True:
        length_input = input("Enter the series length: ").strip()
        if not length_input:
            print("🚫 Error: Length cannot be empty.")
        elif not length_input.isdigit():
            print("🚫 Error: Length must be a positive integer.")
        else:
            length = int(length_input)
            if length < 0:
                print("🚫 Error: length must not be negative.")
            elif length == 0:
                print("🚫 Error: length must be greater than 0.")
            elif length > len(digits):
                print("🚫 Error: length must be smaller than string length.")
            else:
                return length


def main():
    print("🔍 Welcome to the Signal Analyzer")
    print("Analyze number sequence using the Largest Series Product technique.\n")

    while True:
        try:
            digits = prompt_for_digits()
            length = prompt_for_length(digits)
            result = largest_series_product(digits, length)
            print(f"\n✅ Largest product in sequence of series length {length} is: {result}\n")

            # Ask user if they want to analyze another sequence
            again = input("Analyze another sequence?\nEnter 'y' to continue, enter any key to exit: ").strip().lower()
            if again != 'y':
                print("👋 Exit analyzer. Good Bye!")
                break

        except ValueError as ve:
            print(f"❌ Error: {ve}\n")
        except Exception as e:
            print(f"❗ Unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()
