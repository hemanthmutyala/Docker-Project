FROM alpine:latest 
RUN apk update && apk add python3
RUN mkdir /home/data && mkdir /home/output

COPY docr.py /home

WORKDIR /home

CMD ["python3", "docr.py"]