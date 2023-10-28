# Данные находятся в файле kc_house_data.csv.

# Считать данные с помощью pandas.
# Вывести на экран первые 5 строк.

# Создать новый признак price_per_sq_lot, который будет содержать avg = среднюю стоимость за один кв. метр общей площади.

# Создать новый признак delta_renovated, который будет содержать разницу в годах между годом реновации дома и годом постройки дома и сохраните в renv. Если реновации дома не было, то в новом признаке поставьте 0.

# Создайте признаки года продажи, месяца продажи и сохраните в year_ch, month_ch.

# Удалите признаки date, zipcode, lat, long и сохраните в new.

import pandas as pd
df = pd.read_csv('kc_house_data.csv', sep=',')
stroki = df.head()

avg = df['price_per_sq_lot'] = df['price'] / df['sqft_lot']

df['delta_renovared'] = df['yr_renovated'] - df['yr_built']
renv = df['delta_renovared'] = df['delta_renovared'].apply(lambda x: x if x > 0 else 0)

year_ch = df['year'] = df['date'].apply(lambda x: int(x[:4]))
month_ch = df ['month']=df['date'].apply(lambda x: int(x[4:6]))

new = df.drop(columns=['date','zipcode', 'lat', 'long'], inplace=True)