FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3-pip && apt-get clean

WORKDIR /home/backend/

ENV PYTHONUNBUFFERED=1

# requirements.txt의 변경사항이 있을 때 갱신
RUN echo 3

ADD ./requirements.txt /home/backend/requirements.txt

RUN pip3 install -r requirements.txt

# django의 변경사항이 있을 때 갱신
RUN echo 4

ADD ./ /home/backend/

EXPOSE 8000

CMD python3 manage.py collectstatic --noinput --settings=backend.settings.prod \
    && python3 manage.py migrate --settings=backend.settings.prod \
    && gunicorn backend.wsgi:application --bind 8000:8000