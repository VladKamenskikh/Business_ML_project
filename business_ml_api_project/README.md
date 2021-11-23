Итоговый проект курса "Машинное обучение в бизнесе"
Автор: Владислав Каменских

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: Kaggle - https://www.kaggle.com/teejmahal20/airline-passenger-satisfaction
Задача: предсказать уровень удовлетворенности авиационных пассажиров. Бинарная классификация

Используемые признаки:

Inflight wifi service - оценка сервиса Wi-Fi (0-5)
Type of Travel - тип поездки (бизнес или персональная)
Customer Type - тип клиента (лояльный или нет)
Baggage handling - оценка доставки багажа (0-5)
Online boarding - оценка онлайн регистрации (0-5)
Class - класс обслуживания (Business, Eco Plus, Eco)
Inflight service - оценка обслуживания на борту (0-5)
Checkin service - оценка регистрации пассажиров в аэропорту (0-5)
Gate location - оценка расположение посадочных гейтов (0-5)
Seat comfort - оценка удобности сидений (0-5)
Age - возраст пассажира
Cleanliness - оценка чистоты судна (0-5)
Преобразования признаков: LabelEncoder

Модель: CatBoost

Клонируем репозиторий
$ git clone https://github.com/VladKamenskikh/Business_ML_project.git business_ml_api_project
$ cd business_ml_api_project
Запускаем контейнер
$ docker-compose up -d
Можно отправить POST-запрос на 127.0.0.1:8180/predict c полями, указанными в "Признаках"