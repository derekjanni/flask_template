FROM python:3.6-slim as base

RUN apt-get update
RUN apt-get -y install build-essential python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info --fix-missing
RUN apt-get -y install netcat postgresql-9.3 xvfb iputils-ping curl

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install gunicorn
RUN pip install -r requirements.txt
COPY . .

RUN adduser --disabled-password --gecos '' default
RUN chmod +x boot.sh
USER default

FROM base as run
EXPOSE 5005
ENV PYTHONPATH=.:src
CMD ["./boot.sh"]
