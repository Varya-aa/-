print("Список картинок:")
print("1.Вай угрюмая")
print("2.Вай взволнованная")
print("3.Вай ест")
print("4.Вай подмигивает")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
    image = "ВайУгрюмая.png"

if image_number == 2:
    image = "ВайВзволнованная.png"

if image_number == 3:
    image = "ВайЕст.png"

if image_number == 4:
    image = "ВайПодмигивает.png"

print(image)
