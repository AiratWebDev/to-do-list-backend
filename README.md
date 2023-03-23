# Backend-часть приложения для задач (to do list)

### Описание проекта 

Проект для тестового задания. Представляет собой API для вывода списка задач. Отображение и логика реализованы на фронтенде. Проект был выложен на хостинге.

Общий вид:
![image](https://user-images.githubusercontent.com/113205906/223139630-1dae0fdf-6bbc-440f-b8cd-b28f1318efaa.png)

#### Подробнее  
• Backend реализован на Flask + SQLAlchemy.   
• Создана модель для хранения задач. Содержит в себе имя пользователя, его почту, название, текст и статус задачи.  
• Проект задеплоен с помощью Docker-Compose и Nginx.

### Стэк разработки:
• Python 3.11  
• Flask 2.2.3     
• Flask-SQLAlchemy 3.0.3  
• Flask-Migrate 4.0.4  
• Flask-Cors 3.0.10  
• Docker  
• Nginx   

### Запуск

Flask:
```python
flask run
```
Docker-Compose:
```docker
docker compose -f docker-compose.yaml up -d
```
Docker:
```
docker build -t вашеимяобраза .
docker run -d --name вашеимяконтейнера -p 5000:5000 вашеимяобраза
```
