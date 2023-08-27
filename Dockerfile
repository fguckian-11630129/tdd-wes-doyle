FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN python -m spacy download en_core_web_sm

RUN pip install -e .
