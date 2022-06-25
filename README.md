# Пульт охраны банка

Отображает сотрудников, имеющих пропуск в хранилище, а также тех, кто находятся в хранилище в данный момент.

Отображает историю посещения хранилища каждого сотрудника.

### Как установить

Создайте файл окружения `.env` и запишите параметры для подключения к базе данных, которые затем используются в файле `project\settings.py`.

Также в файле `.env` запишите секретный ключ сайта и флаг отладки.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Запуск сайта:
```
python manage.py runserver 0.0.0.0:8000
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).