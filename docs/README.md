
# Цифровой ассистент преподавателя

## Описание проекта
Проект представляет собой сайт по проекту "Цифровой ассистент преподавателя", который направлен на упрощение рутинных задач преподавателя с помощью веб-интерфейса и ИИ-модуля. Ассистент помогает составлять рабочую программу, фиксировать успеваемость и генерировать обратную связь. Также был создан Telegram-бот, который напоминает о занятиях, позволяет удалять и добавлять их по дням недели.

---

## Создание Telegram-бота

Для создания Telegram-бота использовалась библиотека `python-telegram-bot`. Процесс разработки включал следующие этапы:

- Регистрация бота у BotFather в Telegram
- Написание Python-скрипта для взаимодействия с Telegram API
- Реализация функционала расписания, напоминаний и управления занятиями
- Использование SQLite для хранения данных о парах и расписании
- Добавление inline-кнопок для навигации и настройки напоминаний

Подробный гайд взят из статьи: [How to Create a Telegram Bot Using Python](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)

---

## Создание сайта проекта

Сайт разработан с использованием HTML и Markdown для удобства написания и редактирования содержимого. Структура сайта включает:

- Главная страница с описанием проекта
- Страницу "О проекте"
- Раздел "Участники"
- Журнал прогресса с тремя записями
- Раздел "Ресурсы" с полезными ссылками

Для создания сайта проекта был использован шаблон Bootstrap, который обеспечивает адаптивный и современный дизайн без необходимости писать весь CSS с нуля. Это ускорило разработку и сделало интерфейс удобным на разных устройствах.

---

## Журнал прогресса

### Запись 1
- Начало разработки Telegram-бота.
- Настроена базовая структура бота, реализован прием и обработка команд.
- Создана база данных для хранения расписания.

### Запись 2
- Добавлены inline-кнопки для удобного взаимодействия.
- Реализованы напоминания за 10 минут, 30 минут и 1 час до пары.
- Начата работа над интерфейсом сайта.

### Запись 3
- Завершена базовая версия сайта.
- Интегрирован Markdown для наполнения страниц.
- Проведено тестирование бота и сайта, исправлены баги.

---

## Используемые технологии

- Python 3
- python-telegram-bot
- SQLite
- HTML
- Markdown
- Git для контроля версий

---

## Контакты и источники

- Статья по созданию Telegram-бота: [freeCodeCamp](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
- Исходный код проекта и дополнительные материалы находятся в репозитории.


