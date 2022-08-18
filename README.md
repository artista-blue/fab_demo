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

### Connect to DB
```
. .env; PGPASSWORD=${db_password} psql -h localhost -p $db_port -U $db_user -d $db_database
```

### Run directly
```
python3 -m venv venv3
source venv3/bin/activate
pip install -r flask/requirements.txt

. .env; PYTHONDONTWRITEBYTECODE=1 DATABASE_URI="postgresql://${db_user}:${db_password}@localhost:${db_port}/${db_database}" python flask/run.py
```
