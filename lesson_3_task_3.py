from Address import Address
from Mailing import Mailing


address_from = Address("101000", "Москва", "Тверская", "1", "10")
address_to = Address("603000", "Нижний Новгород", "Рождественская", "20", "5")


mailing = Mailing(to_address=address_to,
                  from_address=address_from,
                  cost=250.50,
                  track="TRACK12345")


print_string = (f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city},"
                f" {mailing.from_address.street}, {mailing.from_address.building} - {mailing.from_address.apartment} в"
                f" {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street},"
                f" {mailing.to_address.building} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")


print(print_string)
