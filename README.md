# flask_calendar
Для начала установим нужную библиотеку
```pip install flask```

Перейдом в нужный репрозиторий проекта
```cd <rep path>```

Запустим приложение:
```flask --app acme/server.py run```


Выполняем следующие команды: 
Создаем 2 записи в календаре

```curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-05-01|title|text"```

```curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-05-02|title|text"```


Проверяем возможность создавать вторую запись на туже дату

```http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-05-01|title|text"```


Получаем список записей всех и частной

```curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-05-02|title|text"```

```curl http://127.0.0.1:5000/api/v1/calendar/1/```


Проверяем возможно редактирования записи

```curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2025-05-03|title|new text"```



