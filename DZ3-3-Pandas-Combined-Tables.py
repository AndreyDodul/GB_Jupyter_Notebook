# Составьте несколько сводных таблиц.
# Данные находятся в файле kc_house_data.csv.

# 1. Cреднюю стоимость домов в зависимости от количества спален и сохраните в avg.
# Отсортируйте от меньшей стоимости к большей.

# 2. Найдите минимальную min, среднюю mean и максимальную max стоимости домов в зависимости
# от состояния дома и сохраните в price.

# 3. Постройте таблицу с подсчетом количества домов в данных в зависимости от
# вида на набережную waterfront и оценкой вида view и сохраните ее в view_waterfront.

# 4. Каких домов в зависимости от этажности и количества спален больше?
# Постройте эту таблицу, содержащую в себе информацию о спальнях и этажности, и
# сохраните ее в bedrooms_floors.

# 5. Постройте таблицу с подсчетом медианной стоимости домов в данных в зависимости от
# состояния  дома и оценки дома и сохраните в 'median_price'.'''

import pandas as pd
df = pd.read_csv('kc_house_data.csv', sep=',')
df.head()

avg = df.groupby('bedrooms').agg({'price': 'mean'}).sort_values('price')

price = df.groupby('condition').agg({'price': ['min', 'mean', 'max']})

view_waterfront = df.pivot_table(index='waterfront', columns='view', values='id',
 aggfunc='count', fill_value=0)

bedrooms_floors = pd.crosstab(index=df['floors'], columns=['bedrooms'])

median_price = df.pivot_table(index='condition', columns='grade', values='price', aggfunc='median', fill_value=0)
