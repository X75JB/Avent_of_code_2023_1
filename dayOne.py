def calculateCalibration(file_name):
    total = 0

    digit_conversion = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                for word, digit in digit_conversion.items():
                    line = line.replace(word, digit)
                numbers = [char for char in line if char.isdigit()]

                if numbers:
                    first_number = int(numbers[0])
                    last_number = int(numbers[-1])
                    print(first_number, '+', last_number)
                    calibrate = int(str(first_number) + str(last_number))
                    total += calibrate

    return total


filename = 'values.txt'
print(calculateCalibration(filename))
