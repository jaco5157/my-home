FROM python:3

RUN pip3 install flask
RUN pip3 install flask-mysqldb
RUN pip3 install gunicorn

EXPOSE 5000

COPY ./backend/ /

CMD gunicorn main:app -b0.0.0.0:5000