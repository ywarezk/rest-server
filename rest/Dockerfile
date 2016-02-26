FROM python:2.7

RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD . /code
EXPOSE 8000
CMD waitress-serve --port=8000 --threads=10 rest.wsgi:application

