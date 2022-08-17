# Building Web App using Flask-AppBuilder

### Setup
```
docker-compose up -d --build
docker-compose ps
docker exec -it fab_demo_web_1 /bin/bash ./init_db
```

### Login
http://localhost:5000   (user:password: admin:admin)

### Cleanup
```
docker-compose down
rm -rf data
```
