# sample fast api

# Setup

``` shell
uv sync
```

## Todo api

### Get All Todos

``` shell
curl -X 'GET' \
  'http://127.0.0.1:8000/todos?first_n=0' \
  -H 'accept: application/json'
```

### Get Todo

``` shell
curl -X 'GET' \
  'http://127.0.0.1:8000/todos/2' \
  -H 'accept: application/json'
```

### Create Todo

``` shell
curl -X 'POST' \
  'http://127.0.0.1:8000/todos' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "A New Task",
  "description": "Do this task, please.",
  "priority": 1
}'

```

### Update Todo

``` shell
curl -X 'PUT' \
  'http://127.0.0.1:8000/todos?id=6' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Get it done",
  "description": "Right now",
  "priority": 1
}'
```

### Delete Todo

``` shell
curl -X 'DELETE' \
  'http://127.0.0.1:8000/todos/2' \
  -H 'accept: application/json'
```
