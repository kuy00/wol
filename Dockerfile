# install python
FROM python:3.9 as base
RUN apt-get update \
    && apt-get install -y -qq python3-pip netcat-openbsd libpcap0.8

COPY requirements.txt requirements.txt

# python package install
RUN pip install --upgrade pip --root-user-action=ignore \
    && pip install -r requirements.txt --root-user-action=ignore

WORKDIR /var/www

FROM base as app
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]