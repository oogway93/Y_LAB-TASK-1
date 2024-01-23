# Y_LAB Task 1

### *__Y_LAB TASK 1__* is a task for company Y_LAB university. The main assignment was to create an FastAPI app performing Restaurant service.

### Conditions:

Написать проект на FastAPI с использованием PostgreSQL в качестве БД. В проекте следует реализовать REST API по работе с
меню ресторана, все CRUD операции. Для проверки задания, к презентаций будет приложена Postman коллекция с тестами.
Задание выполнено, если все тесты проходят успешно.
Даны 3 сущности: Меню, Подменю, Блюдо.

Зависимости:

- У меню есть подменю, которые к ней привязаны.
- У подменю есть блюда.

Условия:

- Блюдо не может быть привязано напрямую к меню, минуя подменю.
- Блюдо не может находиться в 2-х подменю одновременно.
- Подменю не может находиться в 2-х меню одновременно.
- Если удалить меню, должны удалиться все подменю и блюда этого меню.
- Если удалить подменю, должны удалиться все блюда этого подменю.
- Цены блюд выводить с округлением до 2 знаков после запятой.
- Во время выдачи списка меню, для каждого меню добавлять кол-во подменю и блюд в этом меню.
- Во время выдачи списка подменю, для каждого подменю добавлять кол-во блюд в этом подменю.
- Во время запуска тестового сценария БД должна быть пуста.

1. Firstly, you need to add venv file by this command:
   ```python 
    python -m venv venv
2. Activate the environment (for linux):
   ```python
   source venv/bin/activate
4. Install dependencies:
   ```python
   poetry install
5. Create a ".env" file at the root of the directory with params:
   ```python
   ALL SETTINGS FOR POSTGRESQL
   
   DB_USER=your postgres user
   DB_PASS=your password for user
   DB_NAME=your name of db
   DB_HOST=127.0.0.1 or localhost
   DB_PORT=5432
6. Start an app due this command:
   ```python
   python core.py


