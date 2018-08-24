FROM python:3.6

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

# Expose and run
EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]