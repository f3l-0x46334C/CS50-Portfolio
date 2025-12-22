from sys import argv, exit


def main():
    if len(argv) == 2:
        py_file = argv[1].strip().lower()
        if argv[1].lower().endswith(".py"):
            try:
                with open(py_file) as f:
                    line_count = 0
                    for line in f:
                        if line.strip() == "" or line.lstrip().startswith("#"):
                            continue
                        line_count += 1
                    print(line_count)
            except FileNotFoundError:
                exit("File does not exist")
            except PermissionError:
                exit("Permission denied")
        else:
            exit("Not a Python file")

    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
