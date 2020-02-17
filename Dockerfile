FROM frolvlad/alpine-python3:latest
RUN apk update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["web/app.py"]