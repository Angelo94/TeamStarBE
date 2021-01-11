FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
COPY requirements.txt . 
COPY ./requirements.txt /requirements
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000