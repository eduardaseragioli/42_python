def garden_operations():
    try:
        temp = int("abc")
    except ValueError:
        print("\nTesting ValueError...")
        print("Caught ValueError: invalid literal for int()")

    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("\nTesting ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero")

    try:
        with open('missing.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("\nTesting FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        dictionary = {'flower': 'rose',
                        'tree': 'olive'}
        print(dictionary['missing_plant'])
    except KeyError:
        print("\nTesting KeyError...")
        print("Caught KeyError: 'missing\_plant'")

    print("\nTesting multiple errors together...")
    try:
        temp = int("xyz")
        result = 10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")
