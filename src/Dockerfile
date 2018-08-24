FROM python:3.6

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Move all of the django project files in there
COPY * /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]