from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S21", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 13", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 6", "+79456789012"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79567890123"))

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")