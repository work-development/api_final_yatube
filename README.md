# API для Yatube    

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
