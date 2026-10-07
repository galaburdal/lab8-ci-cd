Лабораторна робота №7
Тема: BDD-підхід в автоматизації

Структура:
features/
├── environment.py
├── login.feature
└── steps/
    ├── __init__.py
    └── login_steps.py
requirements.txt

Встановлення:
python3 -m pip install -r requirements.txt

Основний запуск:
python3 -m behave

Запуск з результатами Allure:
python3 -m behave -f allure_behave.formatter:AllureFormatter -o allure-results

Перегляд Allure:
allure serve allure-results

Примітка:
Для команди "allure serve" окремо потрібен встановлений Allure Commandline.
