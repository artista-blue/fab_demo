FROM python:3.7.5

ARG app_dir=/app/

ADD . $app_dir

WORKDIR $app_dir

RUN apt update -y && apt install -y build-essential libpq-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
