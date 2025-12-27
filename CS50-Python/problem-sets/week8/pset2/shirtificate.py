from fpdf import FPDF


def main():
    user_name = input("Enter your name: ").strip()
    tshirt_text = f"{user_name} took CS50"

    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_page_background((30, 30, 30))
    pdf.set_margin(0)
    pdf.add_page()

    pdf.set_font("helvetica", "B", size=50)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=0, h=50, text="CS50 Shirtificate", align="C")

    pg_width, pg_height = 210, 297
    img_width = 160
    img_height = 160
    x_pos = (pg_width - img_width) / 2
    y_pos = (pg_height - img_height) / 2
    pdf.image("shirtificate.png", x=x_pos, y=y_pos, w=img_width, h=img_height)

    font_size = 25
    pdf.set_font("Helvetica", "B", size=font_size)
    max_width = img_width - 50
    while pdf.get_string_width(tshirt_text) > max_width and font_size > 5:
        font_size -= 2
        pdf.set_font("Helvetica", "B", size=font_size)

    y_text = y_pos + img_height / 2
    pdf.set_y(y_text)
    pdf.cell(w=0, h=-30, text=tshirt_text, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
