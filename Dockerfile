FROM python:alpine3.18

RUN apk add --no-cache bash && \
    rm -rf /var/vache/apk*

RUN python3 -m ensurepip

WORKDIR /var/www/app

COPY . .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/var/www/app"