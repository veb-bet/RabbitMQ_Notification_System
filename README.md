# RabbitMQ Notification System

Простой проект на Python с использованием RabbitMQ, демонстрирующий работу с очередями сообщений.

## Описание

Очередь order_queue — только для заказов. Очередь payment_queue — только для платежей. 
Один consumer слушает order_queue. Другой consumer — payment_queue.

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
- Логин: admin
- Пароль: admin

### Запуск отправителей и получателя

В одном терминале:
```bash
python3 consumer_orders.py
```

В другом терминале:
```bash
python3 consumer_payments.py
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
RabbitMQ_notification_system/
├── docker-compose.yml
├── producer_orders.py
├── producer_payments.py
├── consumer_orders.py  
├── consumer_payments.py
└── README.md
```
---

![image](https://github.com/user-attachments/assets/03ff4dc2-7a7d-4805-86b2-4312827e6bc8)

---
![image](https://github.com/user-attachments/assets/6520d866-3c90-4fe3-90f4-fb3295bfa8f5)


