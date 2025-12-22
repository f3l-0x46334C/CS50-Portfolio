from sys import argv, exit
from tabulate import tabulate
import csv


def main():
    menu_data = []
    if len(argv) == 2:
        csv_file = argv[1].strip().lower()
        if argv[1].lower().endswith(".csv"):
            try:
                with open(csv_file, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                            menu_data.append(list(row.values()))
                    print(
                        tabulate(
                            menu_data,
                            headers=reader.fieldnames,
                            tablefmt="grid",
                        )
                    )
            except FileNotFoundError:
                exit("File does not exist")
            except PermissionError:
                exit("Permission denied")
        else:
            exit("Not a CSV file")

    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
