months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        user_input = input(" Enter date (MM/DD/YYYY) : ").strip()
        try:
            if "/" in user_input:
                m, d, y = user_input.split("/")
                if m.isdigit():
                    m = int(m)
                    if m > 12:
                        raise ValueError
                    m = f"{m:02}"
                else:
                    raise ValueError

            elif "," in user_input:
                user_input = user_input.replace(", ", "/").replace(" ", "/")
                m, d, y = user_input.split("/")

                if m.isalpha():
                    m = m.title()
                    for i in range(len(months)):
                        if m == months[i]:
                            m = f"{i+1}"
                            if len(str(m)) <= 1:
                                m = f"0{i+1}"
                else:
                    raise ValueError
            else:
                raise ValueError

            if d.isdigit():
                d = int(d)
                if d > 31:
                    raise ValueError
                d = f"{d:02}"
            else:
                raise ValueError

            if len(y) != 4 or not y.isdigit():
                raise ValueError
            else:
                y = int(y)

            print(y, m, d, sep="-")
            break

        except ValueError:
            print(" ### WRONG TRY (MM/DD/YYYY) ###")


main()
