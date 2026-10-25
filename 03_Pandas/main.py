import numpy as np
import pandas as pd

s1 = pd.Series([1,2,3])
s2 = pd.Series([8885,00,4])
df = pd.DataFrame({"col1":s1,"col2":s2})
print(df)


df = pd.DataFrame({
    "id": [1, 2, 3],
    "product": ["Keyboard", "Mouse", "Monitor"],
    "price": [1500, 700, 8000],
    "quantity": [2, 3, 1]
})

df["total"] = df["price"] * df["quantity"]

print(df)

sales_data = {'Дата': pd.date_range(start='2024-01-01', periods=10, freq='D'),
            'Продажі': np.random.randint(100, 1000, size=10) }

df_sales_data = pd.DataFrame(sales_data)
print(df_sales_data);
'''
# Запис у csv
print("== Запис у CSV ==")
df_sales_data.to_csv('sales.csv', index=False, encoding='utf-8')
print("Збережено у CSV")
print()

#Читання із csv
print("=== Читання CSV ===")
df_sales_data = pd.read_csv('sales.csv')
print("Прочитані дані з файлу:")
print(df_sales_data.head(3))
print()

df = pd.DataFrame({
    "month": ["Jan", "Jan", "Feb", "Feb"],
    "city": ["Lviv", "Kyiv", "Lviv", "Kyiv"],
    "revenue": [100, 200, 150, 250]
})

wide = df.pivot(
    index="month",
    columns="city",
    values="revenue"
)
print(df)
print(wide)
'''

#Practice
'''
#Завдання 1
У вас є дані про користувачів із полями: "Ім'я", "Вік" і "Місто".
Створіть DataFrame зі словника Python із п'ятьма записами.
Виведіть весь DataFrame.
Визначте кількість рядків і стовпців.
Виведіть назви всіх стовпців.
Покажіть перші три рядки таблиці.
Завдання 2
У файлі CSV збережено дані про фільми: "Назва", "Жанр", "Рік", "Рейтинг".
Прочитайте дані з CSV у DataFrame.
Виведіть перші п'ять рядків таблиці.
Визначте загальну кількість рядків і стовпців.
Визначте типи даних для кожного стовпця.
Перевірте наявність пропусків.
'''
data1 = pd.DataFrame({
    "Name": ["Taras","Ivan","Dmytro","Vova","Nadya"],
    "Age":[20,59,18,98,56],
    "City": ["Lviv","Dubno","Rivne","Odesa","Kharkiv"],
})
print(data1)

rows,columns = data1.shape
print("Number of rows and Columns: ",rows,columns)

print("All columns names: ",data1.columns)
print("Top 3 rows: ", data1.head(3))

