try:
 amount = int(input("Пожалуйста, укажите количество билетов: "))
 age = [int(input("Пожалуйста, укажите возраст посетителя: ")) for n in range(amount)]
 price = (0, 990, 1390)

 i = 0
 new_price = 0

 while i < amount:
     if age[i] < 18:
         new_price += price[0]
         print('- Бесплатный билет')
     elif 18 <= age[i] <= 24:
         new_price += price[1]
         print('- Стоимость билета 990 руб.')
     elif age[i] >= 25:
         new_price += price[2]
         print('- Стоимость билета 1390 руб.')
     i += 1
 if amount > 3:
     new_price = new_price * 0.9
 print("Общая стоимость билетов с учетом скидки (при наличии):", new_price, "руб.")
except ValueError as a:
    print("Количество билетов и возраст гостей должны быть введены цифрами.")
