Использовать python3.7 \
Остальные зависимости описаны в requirements.txt

Задание:

1.Сделать сервис для ведения учёта положенных в доме кирпичей \
Сущности: \
Дом (адрес, год постройки) \
Задание на кладку кирпичей (количество кирпичей) \
Реализовать три метода: \
POST /building/ - создать дом \
POST /building/{id}/add-bricks/ - положить N кирпичей в дом с id в момент времени T.\
GET /stats/ - вывести статистику по всем существующим домам - сколько в каждом\
лежит кирпичей с группировкой по датам. Также необходимо вывести адрес дома.\

Запуск проекта:

Сделать миграции БД из django_pik\
python house_building/manage.py makemigrations\
python house_building/manage.py migrate\
python house_building/manage.py makemigrations core\
python house_building/manage.py migrate core

Запустить тесты из django_pik\
python house_building/manage.oy test core.tests

Запустить приложение из django_pik\
python houser_building/manage.py runserver