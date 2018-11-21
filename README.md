# PostgreSQL model based testing

Этот репозиторий содержит тесты для PostgreSQL.

## Общее описание и решаемые задачи

Ввыполняется :

    Подготовка окружения для тестирования
    Параметризация и запуск тестов

## Запуск тестов .





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