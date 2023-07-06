from math import floor


class Integer:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_float(float_value: float):
        if type(float_value) != float:
            return f"value is not a float"
        return Integer(floor(float_value))

    @staticmethod
    def from_roman(value: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in value[::-1]:
            value = roman_dict[char]

            if value >= prev_value:
                total += value
            else:
                total -= value

            prev_value = value

        return Integer(total)

    @staticmethod
    def from_string(value: str):
        try:
            if type(value) != str:
                raise ValueError

            num = int(value)
            return Integer(num)

        except ValueError:
            return f"wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

