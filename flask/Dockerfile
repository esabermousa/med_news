From python:3.6

LABEL eslam saber "Eslam Saber <e.saber.mousa@gmail.com>"

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENV FLASK_ENV=development

CMD ["uwsgi", "app.ini"]