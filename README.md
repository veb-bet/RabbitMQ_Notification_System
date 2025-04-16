# RabbitMQ Notification System

Простой проект на Python с использованием RabbitMQ, демонстрирующий работу с очередями сообщений.

## Описание

Система состоит из трёх компонентов:

- `producer_orders.py` — отправляет уведомления о **новых заказах**
- `producer_payments.py` — отправляет уведомления о **платежах**
- `consumer.py` — принимает и обрабатывает **все уведомления**

Все взаимодействия происходят через очередь `notification_queue`, реализованную на базе RabbitMQ.

---

## Быстрый старт

### 1. Установи зависимости

Установи библиотеку `pika`:

```bash
pip install pika
```

### 2. Запусти RabbitMQ через Docker
Создай и запусти контейнер с RabbitMQ и web-интерфейсом:

```bash
sudo docker-compose up -d
```

Проверь, что всё работает:

```bash
docker ps
```

### 3. Открой веб-интерфейс RabbitMQ
Перейди в браузере по адресу: http://localhost:15672
Логин: admin
Пароль: admin

### Запуск отправителей и получателя

Шаг 1 — запусти потребителя (consumer):

```bash
python3 consumer.py
```

Шаг 2 — в другом терминале запусти отправителя заказов:

```bash
python3 producer_orders.py
```

Шаг 3 — и ещё один отправитель платежей:

```bash
python3 producer_payments.py
```

### Структура проекта

```bash
mqr/
├── docker-compose.yml         # конфигурация RabbitMQ
├── producer_orders.py         # отправка заказов
├── producer_payments.py       # отправка платежей
├── consumer.py                # приём и обработка всех сообщений
└── README.md
```

### Примечания

Все сообщения отправляются в одну очередь notification_queue.
Потребитель различает типы уведомлений по полю type (new_order, payment).
![image](https://github.com/user-attachments/assets/3a5c6560-61de-4315-a5f1-92e98e79fa6a)


Используется RabbitMQ Management UI для удобства мониторинга.
![image](https://github.com/user-attachments/assets/a3bd8509-78c4-4edd-98eb-c501d8504ff3)


