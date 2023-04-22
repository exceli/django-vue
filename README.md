# Start

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