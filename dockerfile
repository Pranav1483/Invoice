FROM python:3.10-alpine

ENV SECRET_KEY="django-insecure-^p*p@8)709(59a(+czep=gi=53(s)$ch)=c)vt)4^t2ymni-+a"

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]