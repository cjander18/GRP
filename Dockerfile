FROM frolvlad/alpine-python3:latest

ENV FLASK_APP=grp
ENV FLASK_ENV=development

RUN apk update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["wsgi.py"]