FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /simple_blog_engine
WORKDIR /simple_blog_engine

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /simple_blog_engine

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
