## Структура репозитория:
# API - скрипты для загрузки данных с различных бирж
# docker - настройки контенера для разворачивания среды
# data - данные для анализа зависимостей 
# sql - скрипты для хранения данных
# analytics - аналитика (тетрадки Jupyter Notebook)

Состав Docker контейнеров:
1) Postgres (Database)
2) Python (Data Science Module with Jupyter)
3) Python (ETL Module)


#########
Настройка Docker контейнера (MAC или Linux)

1. В командной строке перейти в папку {REPO}/docker/
2. Собрать контейнер с помощью команды

sudo docker-compose --project-name speculator -f docker-compose.yml up --build -d

3. Для запуска командной строки контейнера, выполнить следующую команду:

sudo docker-compose --project-name speculator -f docker-compose.yml run --rm <service_name>


##########
Запуск Jupyter Notebook для аналитики:
1) Необходимо перейти в папку  {REPO}/docker/ 
2) Выполнить следующую команду

sudo docker-compose --project-name speculator -f docker-compose.yml run --rm notebook

3) Все тетрадки будут сохранятся в папке {REPO}/jupyter/

##########
Запуск клиента Postgres:
1) Необходимо перейти в папку  {REPO}/docker/ 
2) Выполнить следующую команду

sudo docker-compose --project-name speculator -f docker-compose.yml run --rm postgres_client

3) Далее можно запускать различные скрипты сразу из Postgres

##########
Загрузка рыночных данных:
1) Перейти в папку {REPO}/scripts/ из SHELL
2) Выполнить команду: 

	python load_data.py

3) Данные загрузятся в папку  {REPO}/data/outdata 
(если контейнер с Postgres Database корректно настроен, то можно изменить функцию загрузки данных - сразу в Postgre)


