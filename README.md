ReportScript
-------------

Скрипт для анализа продуктов из CSV файлов.


Использование
-------------

python main.py \--files <файлы\> \--report <тип\_отчета\>


### Параметры

`--files`: Список CSV файлов для анализа (через пробел)

`--report`: Тип отчета (доступно: `average-rating`)

### Пример

`python main.py \--files products1.csv products2.csv \--report average-rating`

### Результат

Скрипт выводит таблицу с средними рейтингами брендов:

![результат выполнения скрипта](https://github.com/user-attachments/assets/a16cecf0-a05d-41d9-8b2c-f3d96bfefea8)



Требования
----------

*   Python 3.x
*   CSV файлы
