# Start

## Install
```
git clone https://github.com/exceli/django-vue.git

cd django-vue
```
Rename .env.example to .env and register your settings.

### Backend:
```
cd backend

docker-compose up
```

If you want to create a superuser:

```
docker exec -it app python manage.py createsuperuser
```

### Frontend:
```
cd frontend/frontend

docker-compose up
```

After the start, the server and user parts will be available on 8000 and 8081 ports, respectively.