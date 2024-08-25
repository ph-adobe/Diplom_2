## Дипломный проект. Задание 2: API-тесты
Автотесты для проверки API программы, которая помогает заказать бургер в Stellar Burgers

Созданы API-тесты, покрывающие API ручки login, make_order, update_user_data, registration

### Структура проекта
praktikum - пакет, содержащий код программы tests - пакет, содержащий тесты, разделенные по проверяемым ручкам.

### Установка зависимостей
pip install -r requirements.txt

### Запуск автотестов и создание allure-отчета

Запустить тесты
```
pytest -v
```
Сгенерировать отчет в allure
```
pytest tests --alluredir=allure_results
```

Сформировать отчёт в формате веб-страницы
```
allure serve allure_results
```
