def create_fibonacci_sequence(count:int):
    sequence = [0, 1]
    while len(sequence) != count:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def locate_number(number:int, sequence:list):
    if number in sequence:
        return f"The number - {number} is at index {sequence.index(number)}"

    return f"The number {number} is not in the sequence"
