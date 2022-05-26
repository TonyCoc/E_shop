FROM python:3.10-alpine
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY . .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD gunicorn e_shop.wsgi:application --bind 0.0.0.0:$PORT