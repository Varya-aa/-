from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text = input("Введите текст, который вы хотели бы, чтобы был вверху: ")
bottom_text = input("Введите текст, который вы хотели бы, чтобы был снизу: ")

print(top_text, bottom_text)

print("Список картинок:")
print("1.Вай угрюмая")
print("2.Вай взволнованная")
print("3.Вай ест")
print("4.Вай подмигивает")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
    image_file = "ВайУгрюмая.png"

if image_number == 2:
    image_file = "ВайВзволнованная.png"

if image_number == 3:
    image_file = "ВайЕст.png"

if image_number == 4:
    image_file = "ВайПодмигивает.png"

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size = 70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font = font, fill = 'white')

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font = font, fill = 'white')

image.save('new_meme.png')