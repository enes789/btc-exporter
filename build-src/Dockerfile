FROM python:alpine3.15

RUN apk update && apk add --upgrade python3-tkinter
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /

ENTRYPOINT ["python"]

CMD ["/app.py"]