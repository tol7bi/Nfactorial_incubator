# Nfactorial incubator
Веб-каталог фильмов для тестового задания в рамках конкурсного отбора Nfactorial Incubator

## Установка

Инициализация виртуального окружения:

cd /nfac

source venv/bin/activate 

Установка зависимстей:

pip install -r requirements.txt


Запускаем джанго сервер:

cd /nfac

python3 manage.py runserver

Адрес веб - сайта - http://127.0.0.1:8000/

## Разработка

Проект написан на фреймворке джанго с использованием внутренних шаблонов.
Для сбора информации используются OMDB api и TMDB api.