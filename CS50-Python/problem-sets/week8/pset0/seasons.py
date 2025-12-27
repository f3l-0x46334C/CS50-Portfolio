from datetime import date, datetime
from sys import exit
import re
import inflect


def main():
    ie = inflect.engine()

    birth_date = input(" Enter your birthdate : ")
    input_validation(birth_date)

    minutes = convert(calc_days(birth_date))

    words_output = ie.number_to_words(minutes)
    output_without_and = remove_and(words_output).capitalize()
    print(f"{output_without_and} minutes")


def input_validation(bd):
    """
    pattern from year 1900 to 2025, 12 months, 31 days
    """
    pattern = r"^(19\d{2}|20(0\d|1\d|2[0-5]))-{1}(0[1-9]|1[0-2])\-{1}(0[1-9]|[12][0-9]|3[01])$"
    match = re.search(pattern, bd)

    if not match:
        exit("Invalid date format!")


def calc_days(bd):
    """
    calculate difference between birthdate and today in days
    """
    today = date.today()
    birth_date = datetime.strptime(bd, "%Y-%m-%d").date()
    delta = date.__sub__(today, birth_date)
    return delta.days


def convert(days):
    """
    convert days to minutes
    """
    return days * (24 * 60)


def remove_and(output):
    """
    remove the word 'and' from the number-to-words output
    """
    pattern = r"\sand\s"
    return re.sub(pattern, " ", output)


if __name__ == "__main__":
    main()
