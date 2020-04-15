# Python test

### Спроектировать небольшое приложение на Django "Управление обучением"

* В платформе есть курсы разной направленности.
* Курсы состоят из уроков.
* Уроки могут состоять из текстовых данных, ссылок на файлы/видео.
* Реализовывать админку не нужно, только API для работы со всеми объектами.
* Реализовывать системы авторизации/аутентификации не нужно.

### Схема моделей БД

#### Сущности

* Направление (Direction)
* Курс (Course)
* Урок (Lesson)
* Материал к уроку (LessonMaterial)

### API для этой схемы

#### Endpoints

* Создать/редактировать направление/курс/урок
* Получить список направлений/курсов
* Получить деталку курса/урока
* Создать/редактировать материал
* Связать урок/уроки и курс
* Связать материал/материалы и урок

### Требования

* Python 3.7+
* Django 2.2+
* Django Rest Framework
* PostgreSQL 10+

### API

#### Направления

- GET /api/directions/ - Получить все направления
- POST /api/directions/ - Добавить направление
```
{
    "direction": {
        "title": "Название",
        "position": 1 
    }
}
```
- PUT /api/directions/:id - Редактировать направление
```
{
    "direction": {
        "title": "Новое название",
        "position": 2 
    }
}
```
- DELETE /api/directions/:id - Удалить направление

#### Курсы

- GET /api/courses/ - Получить все курсы
- GET /api/courses/:id - Получить курс по id
- POST /api/courses/ - Добавить курс
```
{
    "course": {
        "title": "Название",
        "position": 1,
        "direction": 1,
        "lessons": [1,2,3]
    }
}
```
- PUT /api/courses/:id - Редактировать курс
```
{
    "course": {
        "title": "Новое название",
        "position": 2,
        "direction": 2,
        "lessons": [] - отвязать все курсы, если пустой массив
    }
}
```
- DELETE /api/courses/:id - Удалить курс

#### Уроки

- GET /api/lessons/ - Получить все уроки
- GET /api/lessons/:id - Получить урок по id 
- POST /api/lessons/ - Добавить урок
```
{
    "lesson": {
        "title": "Название",
        "position": 1,
        "anons": "Анонс",
        "description": "Описание",
        "link_to_video": "/link/to/video",
        "link_to_file": "/link/to/file",
        "materials": [1,2,3,4]
    }
}
```
- PUT /api/lessons/:id - Редактировать урок
```
{
    "lesson": {
        "title": "Новое название",
        "position": 2,
        "anons": "Анонс",
        "description": "Описание",
        "link_to_video": "/link/to/video",
        "link_to_file": "/link/to/file",
        "materials": [] - отвязать все материалы, если пустой массив
    }
}
```
- DELETE /api/lessons/:id - Удалить урок

#### Материалы для уроков

- GET /api/lessons-material/ - Получить все материалы
- GET /api/lessons-material/:id - Получить материал по id 
- POST /api/lessons-material/ - Добавить материал
```
{
    "lesson_material": {
        "title": "Название",
        "material1": "Какой то текст",
        "material2": "Какой то текст",
        "material3": "/link/to/image",
        "material4": "/link/to/file"
        
    }
}
```
- PUT /api/lessons-material/:id - Редактировать материал
```
{
    "lesson_material": {
        "title": "Новое название",
        "material1": "Какой то текст на замену",
        "material2": "Какой то текст на замену",
        "material3": "/link/to/image",
        "material4": "/link/to/file"
    }
}
```
- DELETE /api/lessons-material/:id - Удалить материал