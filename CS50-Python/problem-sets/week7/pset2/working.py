import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    start_hour, start_min, start_period, end_hour, end_min, end_period = validation(s)
    return f"{to_24(start_hour, start_min, start_period)} to {to_24(end_hour, end_min, end_period)}"


def validation(input_text):
    match = re.search(
        r"^([1-9]|1[0-2])(?::([0-5]?[0-9]))?\s+(AM|PM)\s+to\s+([1-9]|1[0-2])(?::([0-5]?[0-9]))?\s+(AM|PM)$",
        input_text,
        re.IGNORECASE,
    )
    if not match:
        raise ValueError

    start_hour = int(match.group(1))
    # if minute exists
    start_min = int(match.group(2)) if match.group(2) else 0
    start_period = match.group(3).upper()

    end_hour = int(match.group(4))
    # if minute exists
    end_min = int(match.group(5)) if match.group(5) else 0
    end_period = match.group(6).upper()

    return start_hour, start_min, start_period, end_hour, end_min, end_period


def to_24(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # if period == "PM"
        if hour != 12:
            hour += 12
    return f"{hour:02d}:{minute:02d}"


if __name__ == "__main__":
    main()
