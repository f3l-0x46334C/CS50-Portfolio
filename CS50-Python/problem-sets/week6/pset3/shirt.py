from sys import argv, exit
from os import path
from PIL import Image, ImageOps


def main():

    if len(argv) == 3:
        valid_exts = (".jpg", ".jpeg", ".png")
        if argv[1].lower().endswith(valid_exts) and argv[2].lower().endswith(
            valid_exts
        ):
            image_file1 = argv[1].strip().lower()
            image_file2 = argv[2].strip().lower()
            _, input_ext = path.splitext(argv[1])
            _, output_ext = path.splitext(argv[2])
            if input_ext.lower() != output_ext.lower():
                exit("Input and output have different extensions")
            else:
                if not path.exists(image_file1):
                    exit("Input does not exist")
                try:
                    # Open Images
                    shirt = Image.open("shirt.png")
                    input_image = Image.open(image_file1)
                    
                    # Resize and crop input image to match shirt size
                    input_image = ImageOps.fit(input_image, shirt.size)
                    # Paste shirt onto input image, preserving transparency
                    input_image.paste(shirt, (0, 0), shirt)
                    # Save the final image
                    input_image.save(image_file2)

                except FileNotFoundError:
                    exit("File not found")
                except PermissionError:
                    exit("Permission denied")

        else:
            exit("Invalid input")

    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
