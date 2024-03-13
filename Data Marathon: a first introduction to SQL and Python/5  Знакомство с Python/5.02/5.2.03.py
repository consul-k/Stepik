avia_ticket_price = 13400
avia_pass_qnt = 2
hotel_night_price = 2100
hotel_night_qnt = 6
car_rent_daily_price = 4500
car_rent_days_qnt = 3

final_price = avia_ticket_price * avia_pass_qnt + hotel_night_price * hotel_night_qnt + car_rent_daily_price * car_rent_days_qnt

print ('Итоговая стоимость путешествия =', final_price)
print ('Стоимость путешествия для одного человека =', final_price/avia_pass_qnt)
