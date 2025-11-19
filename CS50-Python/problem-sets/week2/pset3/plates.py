# Implementing additional functions due to CS50 Problem Set description

def main():
    plate = input(" Enter License plate : ")
    if plate_validation(plate):
        print("Valid")
    else:
        print("Invalid")


def start_letter_validation(plate_text) -> bool:
    for char in plate_text[:2]:
        if char.isdigit():
            return False

    return True


def lenght_check(plate_text) -> bool:
    char_count = 0
    for _ in plate_text:
        char_count += 1

    return True if char_count > 2 and char_count <= 6 else False


def check_number_pos(plate_text) -> bool:
    last_char = None
    num_in_middle = False

    for i in range(len(plate_text)):
        if (
            not plate_text[i].isdigit()
            and last_char is not None
            and last_char.isdigit()
        ):
            num_in_middle = True
            break
        last_char = plate_text[i]

    return False if num_in_middle == True else True


def check_first_number(plate_text) -> bool:
    for char in plate_text:
        if char.isdigit():
            if char == "0":
                return False
            break

    return True


def check_chars(plate_text) -> bool:
    return True if plate_text.isalnum() == True else False


def plate_validation(user_plate) -> bool:
    if (
        start_letter_validation(user_plate)
        and lenght_check(user_plate)
        and check_number_pos(user_plate)
        and check_first_number(user_plate)
        and check_chars(user_plate)
    ):
        return True


main()
