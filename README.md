# API для Yatube 

### POSTS

- ```api/v1/posts/``` (GET) Получить список всех публикаций    

Пример ответа:    

```
[
  {
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
  }
]

```

- ```api/v1/posts/``` (POST)

Пример запроса:    

```
{
"text": "string"
}

```

Пример ответа:    

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}

```

- ```api/v1/posts/{id}/``` Получить публикацию по id    

Ответ в случае когда публикация с данным id есть

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```

Ответ в случае когда публикация с данным id нет   

```
{
  "field_name": [
    "string"
  ]
}

```

- ```api/v1/posts/{id}/``` (PUT) Обновить публикацию по id

Пример запроса:

```
{
  "text": "string"
}

```

Пример ответа:   

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"

```

Ответ в случае когда публикации с данным id не существует, то     

```
{
  "field_name": [
    "string"
  ]
}

```

-  ```api/v1/posts/{id}/``` (PATCH)  Частично обновить публикацию по id   (возможные запросы и ответы совпадают со случаем ```api/v1/posts/{id}/``` (PUT))   
-  ```api/v1/posts/{id}/``` (DELETE) Удалить публикацию по id    

### COMMENTS     

- ```api/v1/posts/{post_id}/comments/``` (GET) Получить список всех комментариев публикации      

Пример ответа:    

```
[
  {
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
  }
]

```


-  ```api/v1/posts/{post_id}/comments/ ``` (POST) Создать новый комментарий для публикации   
-  ```api/v1/posts/{post_id}/comments/{comment_id}/ ```
  (GET) Получить комментарий для публикации по id   
  (PUT) Обновить комментарий для публикации по id    
  (PATCH) Частично обновить комментарий для публикации по id    
  (DELETE) Удалить комментарий для публикации по id
