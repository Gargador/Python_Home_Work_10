# Задание 44 | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

```python
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание пустого DataFrame для one-hot кодирования
one_hot_data = pd.DataFrame()

# Перебор уникальных значений в столбце 'whoAmI'
for value in data['whoAmI'].unique():
    # Создание нового столбца с названием уникального значения
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

one_hot_data.head()
```

# Результат работы кода будет DataFrame в one-hot виде, где каждая уникальная категория из столбца 'whoAmI' будет представлена отдельным столбцом с значениями 0 и 1, где 1 указывает, что элемент принадлежит к данной категории.
