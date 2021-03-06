FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin libgeos-dev libgdal-dev
COPY . /code/
ENTRYPOINT ["sh", "/code/docker-entrypoint.sh"]