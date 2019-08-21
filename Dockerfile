FROM python:3

EXPOSE 5000

ADD look_up.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./look_up.py"]