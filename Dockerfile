# install python
FROM python:3.9 as base
RUN apt-get update \
    && apt-get install -y -qq python3-pip netcat-openbsd

COPY requirements.txt requirements.txt

# python package install
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /var/www

# app
FROM base as app
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]