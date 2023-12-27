# install python
FROM python:3.9 as base
RUN apt-get update \
    && apt-get install -y -qq python3-pip netcat-openbsd

COPY requirements.txt requirements.txt

# python package install
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /var/www

# production-stage
FROM base as production-stage
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]