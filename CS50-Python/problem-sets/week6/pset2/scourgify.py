from sys import argv, exit
import csv


def main():

    if len(argv) == 3:
        csv_file1 = argv[1].strip().lower()
        csv_file2 = argv[2].strip().lower()
        if argv[1].lower().endswith(".csv") and argv[2].lower().endswith(".csv"):
            try:
                with open(csv_file1, "r") as f, open(csv_file2, "w", newline="") as g:
                    # read first csv
                    reader = csv.DictReader(f)

                    # write first csv
                    writer = csv.DictWriter(g, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in reader:
                        last, first = row["name"].split(",")
                        writer.writerow(
                            {
                                "first": first.strip(),
                                "last": last.strip(),
                                "house": row["house"],
                            }
                        )

            except FileNotFoundError:
                exit("File does not exist")
            except PermissionError:
                exit("Permission denied")
        else:
            exit("Not a CSV file")

    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
