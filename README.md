# PostgreSQL model based testing

Этот репозиторий содержит тесты для PostgreSQL.

## Общее описание и решаемые задачи


## Запуск тестов .

- Запуск всех тестов:
```
pytest -v
```
- Запуск конкретного теста:
```
pytest -v test_group/test_basic/test_table_fibonacci_number/test_table_fibonacci_number_insert_commit.py
```
- Запуск тестов из директории:
```
pytest -v test_group/test_basic/test_table_fibonacci_number/
```
- Запуск тестов содержащих в имени подстроку (-k):
```
pytest -v  -k gist
```
- Запуск тестов не содержащих в имени подстроку (-k):
```
pytest -v  -k "not gist"
```
- Запуск маркированных тестов (-m):
```
pytest -v  -m test_basic
```
- Запуск всех тестов кроме маркированных (-m):
```
pytest -v  -m "not test_basic"
```
- Флаг -l  включает отображение значений переменных при падении теста:
```
pytest -v  -l
```
- Флаг -s  включает вывод всех сообщений:
```
pytest -v  -l
```

## Системные требования к окружению

- 

## Рекомендации для тестов:

-

## Настройки для запуска тестов:

- Рекомендуется использовать виртуальную среду Python:
```
$ python3 -m venv env

$ source env/bin/activate
(env) $
```
- установить зависимости: 
```
(env) $pip install -r requirements.txt
```
- создание файла mbt_hosts.json пример данного файла находится в файле demo_mbt_hosts.json.
```
"mbt_conn":{
    "database": "mydb",                     -- наименование базы данных
    "superuser": "myuser",                  -- логин супер пользователя 
    "superuser_password": "myuserpassword", -- пароль супер пользователя
    "user": "myuser",                       -- логин пользователя
    "password": "myuserpassword",           -- пароль пользователя
    "cycle_factor": "1"                     -- коэффициент на который умножаеться количество циклов прхождения тестов            -- 
  },
  "mbt_modules":{
    "multimaster": "True"                   -- флаг тестирования мультимастера
  },
  "mbt_hosts": [
    {
      "host": "192.168.122.152",            -- ip адрес ноды
      "node_id": "1",                       -- номер ноды
      "port": "5432",                       -- порт подключения
      "write": "True",                      -- разрешена или нет запись на данной ноде
      "read": "True"                        -- разрешено чтение с данной ноды
    },
    {
      "host": "192.168.122.56",
      "node_id": "2",
      "port": "5432",
      "write": "True",
      "read" : "True"
    },
    {
      "host": "192.168.122.196",
      "node_id": "3",
      "port": "5432",
      "write": "False",
      "read" : "True"
    }
```



### Настройки ОС для тестирования

- 
