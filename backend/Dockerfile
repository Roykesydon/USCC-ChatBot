FROM python:3.9.12

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

# CMD python app.py
CMD gunicorn -w 4 -b 0.0.0.0:80 app:app
# CMD waitress-serve --listen=*:5000 app:app