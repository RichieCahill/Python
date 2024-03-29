"""DAY1_Part2"""

from functools import cache
from pathlib import Path


@cache
def check_sub_string(sub_string: str) -> str | None:
    """Checks if the given sub_string contains any number words and returns the corresponding digit.

    Args:
        sub_string (str): The input sub_string to check.

    Returns:
        str or None: The corresponding digit if a number word is found in the sub_string, None otherwise.
    """
    number_lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for word in number_lookup:
        if word in sub_string:
            return number_lookup[word]

    return None


def find_left_number(line: str) -> int:
    """Finds the leftmost number in a given line.

    Args:
        line (str): The input line.

    Returns:
        int: The leftmost number found in the line.
    """
    sub_string = ""
    for char in line:
        sub_string += char
        if number := check_sub_string(sub_string):
            return number
        if char.isdigit():
            return char
    error_msg = "No number found in string."
    raise ValueError(error_msg)


def find_right_number(line: str) -> int:
    """Finds the right number in a given line.

    Args:
        line (str): The input line.

    Returns:
        int: The right number found in the line.
    """
    sub_string = ""
    for char in line[::-1]:
        sub_string = char + sub_string
        if number := check_sub_string(sub_string):
            return number
        if char.isdigit():
            return char
    error_msg = "No number found in string."
    raise ValueError(error_msg)


def find_number(line: str) -> int:
    """Find the number in a string by combining the leftmost and rightmost numbers.

    Args:
        line (str): The input string.

    Returns:
        int: The number found in the string.
    """
    return int(find_left_number(line) + find_right_number(line))


def main() -> None:
    """This function reads input data from a file and calculates the sum of numbers

    returned by the find_number function for each line in the input data.

    Returns:
        The sum of numbers returned by the find_number function.
    """
    input_file = Path("./Advent_of_code/2023/DAY1_Part2.txt")
    input_data = input_file.read_text().splitlines()

    print(sum([find_number(line) for line in input_data]))


if __name__ == "__main__":
    main()
